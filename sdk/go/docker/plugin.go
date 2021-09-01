// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package docker

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// <!-- Bug: Type and Name are switched -->
// Manages the lifecycle of a Docker plugin.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-docker/sdk/v3/go/docker"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := docker.NewPlugin(ctx, "sample_volume_plugin", &docker.PluginArgs{
// 			Alias:         pulumi.String("sample-volume-plugin"),
// 			EnableTimeout: pulumi.Int(60),
// 			Enabled:       pulumi.Bool(false),
// 			Envs: pulumi.StringArray{
// 				pulumi.String("DEBUG=1"),
// 			},
// 			ForceDestroy:        pulumi.Bool(true),
// 			ForceDisable:        pulumi.Bool(true),
// 			GrantAllPermissions: pulumi.Bool(true),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// <!-- schema generated by tfplugindocs -->
// ## Schema
//
// ### Required
//
// - **name** (String) Docker Plugin name
//
// ### Optional
//
// - **alias** (String) Docker Plugin alias
// - **enable_timeout** (Number) HTTP client timeout to enable the plugin
// - **enabled** (Boolean) If `true` the plugin is enabled. Defaults to `true`
// - **env** (Set of String) The environment variables in the form of `KEY=VALUE`, e.g. `DEBUG=0`
// - **force_destroy** (Boolean) If true, then the plugin is destroyed forcibly
// - **force_disable** (Boolean) If true, then the plugin is disabled forcibly
// - **grant_all_permissions** (Boolean) If true, grant all permissions necessary to run the plugin
// - **grant_permissions** (Block Set) Grant specific permissions only (see below for nested schema)
// - **id** (String) The ID of this resource.
//
// ### Read-Only
//
// - **plugin_reference** (String) Docker Plugin Reference
//
// <a id="nestedblock--grant_permissions"></a>
// ### Nested Schema for `grantPermissions`
//
// Required:
//
// - **name** (String) The name of the permission
// - **value** (Set of String) The value of the permission
//
// ## Import
//
// Import is supported using the following syntax#!/bin/bash
//
// ```sh
//  $ pulumi import docker:index/plugin:Plugin sample-volume-plugin "$(docker plugin inspect -f {{.ID}} tiborvass/sample-volume-plugin:latest)"
// ```
type Plugin struct {
	pulumi.CustomResourceState

	// Docker Plugin alias
	Alias pulumi.StringOutput `pulumi:"alias"`
	// HTTP client timeout to enable the plugin
	EnableTimeout pulumi.IntPtrOutput `pulumi:"enableTimeout"`
	// If `true` the plugin is enabled. Defaults to `true`
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// The environment variables in the form of `KEY=VALUE`, e.g. `DEBUG=0`
	Envs pulumi.StringArrayOutput `pulumi:"envs"`
	// If true, then the plugin is destroyed forcibly
	ForceDestroy pulumi.BoolPtrOutput `pulumi:"forceDestroy"`
	// If true, then the plugin is disabled forcibly
	ForceDisable pulumi.BoolPtrOutput `pulumi:"forceDisable"`
	// If true, grant all permissions necessary to run the plugin
	GrantAllPermissions pulumi.BoolPtrOutput `pulumi:"grantAllPermissions"`
	// Grant specific permissions only
	GrantPermissions PluginGrantPermissionArrayOutput `pulumi:"grantPermissions"`
	// Docker Plugin name
	Name pulumi.StringOutput `pulumi:"name"`
	// Docker Plugin Reference
	PluginReference pulumi.StringOutput `pulumi:"pluginReference"`
}

// NewPlugin registers a new resource with the given unique name, arguments, and options.
func NewPlugin(ctx *pulumi.Context,
	name string, args *PluginArgs, opts ...pulumi.ResourceOption) (*Plugin, error) {
	if args == nil {
		args = &PluginArgs{}
	}

	var resource Plugin
	err := ctx.RegisterResource("docker:index/plugin:Plugin", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPlugin gets an existing Plugin resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPlugin(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PluginState, opts ...pulumi.ResourceOption) (*Plugin, error) {
	var resource Plugin
	err := ctx.ReadResource("docker:index/plugin:Plugin", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Plugin resources.
type pluginState struct {
	// Docker Plugin alias
	Alias *string `pulumi:"alias"`
	// HTTP client timeout to enable the plugin
	EnableTimeout *int `pulumi:"enableTimeout"`
	// If `true` the plugin is enabled. Defaults to `true`
	Enabled *bool `pulumi:"enabled"`
	// The environment variables in the form of `KEY=VALUE`, e.g. `DEBUG=0`
	Envs []string `pulumi:"envs"`
	// If true, then the plugin is destroyed forcibly
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// If true, then the plugin is disabled forcibly
	ForceDisable *bool `pulumi:"forceDisable"`
	// If true, grant all permissions necessary to run the plugin
	GrantAllPermissions *bool `pulumi:"grantAllPermissions"`
	// Grant specific permissions only
	GrantPermissions []PluginGrantPermission `pulumi:"grantPermissions"`
	// Docker Plugin name
	Name *string `pulumi:"name"`
	// Docker Plugin Reference
	PluginReference *string `pulumi:"pluginReference"`
}

type PluginState struct {
	// Docker Plugin alias
	Alias pulumi.StringPtrInput
	// HTTP client timeout to enable the plugin
	EnableTimeout pulumi.IntPtrInput
	// If `true` the plugin is enabled. Defaults to `true`
	Enabled pulumi.BoolPtrInput
	// The environment variables in the form of `KEY=VALUE`, e.g. `DEBUG=0`
	Envs pulumi.StringArrayInput
	// If true, then the plugin is destroyed forcibly
	ForceDestroy pulumi.BoolPtrInput
	// If true, then the plugin is disabled forcibly
	ForceDisable pulumi.BoolPtrInput
	// If true, grant all permissions necessary to run the plugin
	GrantAllPermissions pulumi.BoolPtrInput
	// Grant specific permissions only
	GrantPermissions PluginGrantPermissionArrayInput
	// Docker Plugin name
	Name pulumi.StringPtrInput
	// Docker Plugin Reference
	PluginReference pulumi.StringPtrInput
}

func (PluginState) ElementType() reflect.Type {
	return reflect.TypeOf((*pluginState)(nil)).Elem()
}

type pluginArgs struct {
	// Docker Plugin alias
	Alias *string `pulumi:"alias"`
	// HTTP client timeout to enable the plugin
	EnableTimeout *int `pulumi:"enableTimeout"`
	// If `true` the plugin is enabled. Defaults to `true`
	Enabled *bool `pulumi:"enabled"`
	// The environment variables in the form of `KEY=VALUE`, e.g. `DEBUG=0`
	Envs []string `pulumi:"envs"`
	// If true, then the plugin is destroyed forcibly
	ForceDestroy *bool `pulumi:"forceDestroy"`
	// If true, then the plugin is disabled forcibly
	ForceDisable *bool `pulumi:"forceDisable"`
	// If true, grant all permissions necessary to run the plugin
	GrantAllPermissions *bool `pulumi:"grantAllPermissions"`
	// Grant specific permissions only
	GrantPermissions []PluginGrantPermission `pulumi:"grantPermissions"`
	// Docker Plugin name
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a Plugin resource.
type PluginArgs struct {
	// Docker Plugin alias
	Alias pulumi.StringPtrInput
	// HTTP client timeout to enable the plugin
	EnableTimeout pulumi.IntPtrInput
	// If `true` the plugin is enabled. Defaults to `true`
	Enabled pulumi.BoolPtrInput
	// The environment variables in the form of `KEY=VALUE`, e.g. `DEBUG=0`
	Envs pulumi.StringArrayInput
	// If true, then the plugin is destroyed forcibly
	ForceDestroy pulumi.BoolPtrInput
	// If true, then the plugin is disabled forcibly
	ForceDisable pulumi.BoolPtrInput
	// If true, grant all permissions necessary to run the plugin
	GrantAllPermissions pulumi.BoolPtrInput
	// Grant specific permissions only
	GrantPermissions PluginGrantPermissionArrayInput
	// Docker Plugin name
	Name pulumi.StringPtrInput
}

func (PluginArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*pluginArgs)(nil)).Elem()
}

type PluginInput interface {
	pulumi.Input

	ToPluginOutput() PluginOutput
	ToPluginOutputWithContext(ctx context.Context) PluginOutput
}

func (*Plugin) ElementType() reflect.Type {
	return reflect.TypeOf((*Plugin)(nil))
}

func (i *Plugin) ToPluginOutput() PluginOutput {
	return i.ToPluginOutputWithContext(context.Background())
}

func (i *Plugin) ToPluginOutputWithContext(ctx context.Context) PluginOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PluginOutput)
}

func (i *Plugin) ToPluginPtrOutput() PluginPtrOutput {
	return i.ToPluginPtrOutputWithContext(context.Background())
}

func (i *Plugin) ToPluginPtrOutputWithContext(ctx context.Context) PluginPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PluginPtrOutput)
}

type PluginPtrInput interface {
	pulumi.Input

	ToPluginPtrOutput() PluginPtrOutput
	ToPluginPtrOutputWithContext(ctx context.Context) PluginPtrOutput
}

type pluginPtrType PluginArgs

func (*pluginPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Plugin)(nil))
}

func (i *pluginPtrType) ToPluginPtrOutput() PluginPtrOutput {
	return i.ToPluginPtrOutputWithContext(context.Background())
}

func (i *pluginPtrType) ToPluginPtrOutputWithContext(ctx context.Context) PluginPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PluginPtrOutput)
}

// PluginArrayInput is an input type that accepts PluginArray and PluginArrayOutput values.
// You can construct a concrete instance of `PluginArrayInput` via:
//
//          PluginArray{ PluginArgs{...} }
type PluginArrayInput interface {
	pulumi.Input

	ToPluginArrayOutput() PluginArrayOutput
	ToPluginArrayOutputWithContext(context.Context) PluginArrayOutput
}

type PluginArray []PluginInput

func (PluginArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*Plugin)(nil))
}

func (i PluginArray) ToPluginArrayOutput() PluginArrayOutput {
	return i.ToPluginArrayOutputWithContext(context.Background())
}

func (i PluginArray) ToPluginArrayOutputWithContext(ctx context.Context) PluginArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PluginArrayOutput)
}

// PluginMapInput is an input type that accepts PluginMap and PluginMapOutput values.
// You can construct a concrete instance of `PluginMapInput` via:
//
//          PluginMap{ "key": PluginArgs{...} }
type PluginMapInput interface {
	pulumi.Input

	ToPluginMapOutput() PluginMapOutput
	ToPluginMapOutputWithContext(context.Context) PluginMapOutput
}

type PluginMap map[string]PluginInput

func (PluginMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*Plugin)(nil))
}

func (i PluginMap) ToPluginMapOutput() PluginMapOutput {
	return i.ToPluginMapOutputWithContext(context.Background())
}

func (i PluginMap) ToPluginMapOutputWithContext(ctx context.Context) PluginMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PluginMapOutput)
}

type PluginOutput struct {
	*pulumi.OutputState
}

func (PluginOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Plugin)(nil))
}

func (o PluginOutput) ToPluginOutput() PluginOutput {
	return o
}

func (o PluginOutput) ToPluginOutputWithContext(ctx context.Context) PluginOutput {
	return o
}

func (o PluginOutput) ToPluginPtrOutput() PluginPtrOutput {
	return o.ToPluginPtrOutputWithContext(context.Background())
}

func (o PluginOutput) ToPluginPtrOutputWithContext(ctx context.Context) PluginPtrOutput {
	return o.ApplyT(func(v Plugin) *Plugin {
		return &v
	}).(PluginPtrOutput)
}

type PluginPtrOutput struct {
	*pulumi.OutputState
}

func (PluginPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Plugin)(nil))
}

func (o PluginPtrOutput) ToPluginPtrOutput() PluginPtrOutput {
	return o
}

func (o PluginPtrOutput) ToPluginPtrOutputWithContext(ctx context.Context) PluginPtrOutput {
	return o
}

type PluginArrayOutput struct{ *pulumi.OutputState }

func (PluginArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Plugin)(nil))
}

func (o PluginArrayOutput) ToPluginArrayOutput() PluginArrayOutput {
	return o
}

func (o PluginArrayOutput) ToPluginArrayOutputWithContext(ctx context.Context) PluginArrayOutput {
	return o
}

func (o PluginArrayOutput) Index(i pulumi.IntInput) PluginOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Plugin {
		return vs[0].([]Plugin)[vs[1].(int)]
	}).(PluginOutput)
}

type PluginMapOutput struct{ *pulumi.OutputState }

func (PluginMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Plugin)(nil))
}

func (o PluginMapOutput) ToPluginMapOutput() PluginMapOutput {
	return o
}

func (o PluginMapOutput) ToPluginMapOutputWithContext(ctx context.Context) PluginMapOutput {
	return o
}

func (o PluginMapOutput) MapIndex(k pulumi.StringInput) PluginOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Plugin {
		return vs[0].(map[string]Plugin)[vs[1].(string)]
	}).(PluginOutput)
}

func init() {
	pulumi.RegisterOutputType(PluginOutput{})
	pulumi.RegisterOutputType(PluginPtrOutput{})
	pulumi.RegisterOutputType(PluginArrayOutput{})
	pulumi.RegisterOutputType(PluginMapOutput{})
}
