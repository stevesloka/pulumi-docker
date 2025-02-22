// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package provider

import (
	"fmt"
	"path/filepath"
	"unicode"

	"github.com/pulumi/pulumi-docker/provider/v3/pkg/version"
	"github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfbridge"
	shimv2 "github.com/pulumi/pulumi-terraform-bridge/v3/pkg/tfshim/sdk-v2"
	"github.com/pulumi/pulumi/sdk/v3/go/common/tokens"
	"github.com/terraform-providers/terraform-provider-docker/shim"
)

const (
	// dockerPkg is the root package name for the Docker package.
	dockerPkg = "docker"

	// dockerMod is the root module for unparented Docker resources.
	dockerMod = "index"
)

// dockerMember manufactures a type token for the docker package and the given module and type.
func dockerMember(mod string, mem string) tokens.ModuleMember {
	return tokens.ModuleMember(dockerPkg + ":" + mod + ":" + mem)
}

// dockerType manufactures a type token for the docker package and the given module and type.
func dockerType(mod string, typ string) tokens.Type {
	return tokens.Type(dockerMember(mod, typ))
}

// dockerResource manufactures a standard resource token given a module and resource name.  It automatically uses the
// docker package and names the file by simply lower casing the resource's first character.
func dockerResource(mod string, res string) tokens.Type {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return dockerType(mod+"/"+fn, res)
}

// dockerDataSource manufactures a data source toeken given a module and resource name.
func dockerDataSource(mod string, res string) tokens.ModuleMember {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return dockerMember(mod+"/"+fn, res)
}

func Provider() tfbridge.ProviderInfo {
	p := shimv2.NewProvider(shim.NewProvider())
	prov := tfbridge.ProviderInfo{
		P:           p,
		Name:        "docker",
		Description: "A Pulumi package for interacting with Docker in Pulumi programs",
		Keywords:    []string{"pulumi", "docker"},
		License:     "Apache-2.0",
		Homepage:    "https://pulumi.io",
		Repository:  "https://github.com/pulumi/pulumi-docker",
		Config: map[string]*tfbridge.SchemaInfo{
			"host": {
				Default: &tfbridge.DefaultInfo{
					Value:   "unix:///var/run/docker.sock",
					EnvVars: []string{"DOCKER_HOST"},
				},
			},
			"registry_auth": {
				Name:        "registryAuth", // not plural
				MaxItemsOne: tfbridge.False(),
			},
		},
		Resources: map[string]*tfbridge.ResourceInfo{
			"docker_config": {
				Tok: dockerResource(dockerMod, "ServiceConfig"),
			},
			"docker_container": {
				Tok:                 dockerResource(dockerMod, "Container"),
				DeleteBeforeReplace: true,
				Fields: map[string]*tfbridge.SchemaInfo{
					// Despite being a list, "command" represents a single command and should not be puralized.
					"command": { // ["echo", "1"]
						Name: "command",
					},
					// This property is named strangely in Terraform, despite allowing multiple entries it is not plural
					// and is not intended to be plural.
					"networks_advanced": {
						Name: "networksAdvanced",
					},
				},
			},
			"docker_image": {
				Tok: dockerResource(dockerMod, "RemoteImage"),
				Fields: map[string]*tfbridge.SchemaInfo{
					"name": {Name: "name"},
				},
			},
			"docker_network":        {Tok: dockerResource(dockerMod, "Network")},
			"docker_secret":         {Tok: dockerResource(dockerMod, "Secret")},
			"docker_service":        {Tok: dockerResource(dockerMod, "Service")},
			"docker_volume":         {Tok: dockerResource(dockerMod, "Volume")},
			"docker_registry_image": {Tok: dockerResource(dockerMod, "RegistryImage")},
			"docker_plugin":         {Tok: dockerResource(dockerMod, "Plugin")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			"docker_network":        {Tok: dockerDataSource(dockerMod, "getNetwork")},
			"docker_registry_image": {Tok: dockerDataSource(dockerMod, "getRegistryImage")},
			"docker_plugin":         {Tok: dockerDataSource(dockerMod, "getPlugin")},
			"docker_image":          {Tok: dockerDataSource(dockerMod, "getRemoteImage")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^3.0.0",
				"semver":         "^5.4.0",
			},
			DevDependencies: map[string]string{
				"@types/node":   "^10.0.0",
				"@types/semver": "^5.4.0",
			},
			Overlay: &tfbridge.OverlayInfo{
				DestFiles: []string{
					"docker.ts",
					"image.ts",
					"utils.ts",
				},
			},
		},
		Python: &tfbridge.PythonInfo{
			Requires: map[string]string{
				"pulumi": ">=3.0.0,<4.0.0",
			},
			Overlay: &tfbridge.OverlayInfo{
				DestFiles: []string{
					"pulumi_docker/docker.py",
					"pulumi_docker/image.py",
					"pulumi_docker/utils.py",
				},
			},
		},
		Golang: &tfbridge.GolangInfo{
			ImportBasePath: filepath.Join(
				fmt.Sprintf("github.com/pulumi/pulumi-%[1]s/sdk/", dockerPkg),
				tfbridge.GetModuleMajorVersion(version.Version),
				"go",
				dockerPkg,
			),
			GenerateResourceContainerTypes: true,
		},
		CSharp: &tfbridge.CSharpInfo{
			PackageReferences: map[string]string{
				"Pulumi": "3.*",
			},
			Namespaces: map[string]string{
				dockerPkg: "Docker",
			},
			Overlay: &tfbridge.OverlayInfo{
				DestFiles: []string{
					"Docker.cs",
					"Image.cs",
					"Extensions.cs",
					"Utils.cs",
				},
			},
		},
	}

	prov.SetAutonaming(255, "-")

	return prov
}
