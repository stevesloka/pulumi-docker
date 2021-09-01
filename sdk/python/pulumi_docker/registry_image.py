# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['RegistryImageArgs', 'RegistryImage']

@pulumi.input_type
class RegistryImageArgs:
    def __init__(__self__, *,
                 build: Optional[pulumi.Input['RegistryImageBuildArgs']] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 keep_remotely: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RegistryImage resource.
        :param pulumi.Input['RegistryImageBuildArgs'] build: Definition for building the image
        :param pulumi.Input[bool] insecure_skip_verify: If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        :param pulumi.Input[bool] keep_remotely: If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from
               the docker registry on destroy operation. Defaults to `false`
        :param pulumi.Input[str] name: The name of the Docker image.
        """
        if build is not None:
            pulumi.set(__self__, "build", build)
        if insecure_skip_verify is not None:
            pulumi.set(__self__, "insecure_skip_verify", insecure_skip_verify)
        if keep_remotely is not None:
            pulumi.set(__self__, "keep_remotely", keep_remotely)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def build(self) -> Optional[pulumi.Input['RegistryImageBuildArgs']]:
        """
        Definition for building the image
        """
        return pulumi.get(self, "build")

    @build.setter
    def build(self, value: Optional[pulumi.Input['RegistryImageBuildArgs']]):
        pulumi.set(self, "build", value)

    @property
    @pulumi.getter(name="insecureSkipVerify")
    def insecure_skip_verify(self) -> Optional[pulumi.Input[bool]]:
        """
        If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        """
        return pulumi.get(self, "insecure_skip_verify")

    @insecure_skip_verify.setter
    def insecure_skip_verify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure_skip_verify", value)

    @property
    @pulumi.getter(name="keepRemotely")
    def keep_remotely(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from
        the docker registry on destroy operation. Defaults to `false`
        """
        return pulumi.get(self, "keep_remotely")

    @keep_remotely.setter
    def keep_remotely(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "keep_remotely", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Docker image.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _RegistryImageState:
    def __init__(__self__, *,
                 build: Optional[pulumi.Input['RegistryImageBuildArgs']] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 keep_remotely: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sha256_digest: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RegistryImage resources.
        :param pulumi.Input['RegistryImageBuildArgs'] build: Definition for building the image
        :param pulumi.Input[bool] insecure_skip_verify: If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        :param pulumi.Input[bool] keep_remotely: If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from
               the docker registry on destroy operation. Defaults to `false`
        :param pulumi.Input[str] name: The name of the Docker image.
        :param pulumi.Input[str] sha256_digest: The sha256 digest of the image.
        """
        if build is not None:
            pulumi.set(__self__, "build", build)
        if insecure_skip_verify is not None:
            pulumi.set(__self__, "insecure_skip_verify", insecure_skip_verify)
        if keep_remotely is not None:
            pulumi.set(__self__, "keep_remotely", keep_remotely)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sha256_digest is not None:
            pulumi.set(__self__, "sha256_digest", sha256_digest)

    @property
    @pulumi.getter
    def build(self) -> Optional[pulumi.Input['RegistryImageBuildArgs']]:
        """
        Definition for building the image
        """
        return pulumi.get(self, "build")

    @build.setter
    def build(self, value: Optional[pulumi.Input['RegistryImageBuildArgs']]):
        pulumi.set(self, "build", value)

    @property
    @pulumi.getter(name="insecureSkipVerify")
    def insecure_skip_verify(self) -> Optional[pulumi.Input[bool]]:
        """
        If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        """
        return pulumi.get(self, "insecure_skip_verify")

    @insecure_skip_verify.setter
    def insecure_skip_verify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure_skip_verify", value)

    @property
    @pulumi.getter(name="keepRemotely")
    def keep_remotely(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from
        the docker registry on destroy operation. Defaults to `false`
        """
        return pulumi.get(self, "keep_remotely")

    @keep_remotely.setter
    def keep_remotely(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "keep_remotely", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Docker image.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sha256Digest")
    def sha256_digest(self) -> Optional[pulumi.Input[str]]:
        """
        The sha256 digest of the image.
        """
        return pulumi.get(self, "sha256_digest")

    @sha256_digest.setter
    def sha256_digest(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sha256_digest", value)


class RegistryImage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 build: Optional[pulumi.Input[pulumi.InputType['RegistryImageBuildArgs']]] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 keep_remotely: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        <!-- Bug: Type and Name are switched -->
        Manages the lifecycle of docker image/tag in a registry.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_docker as docker

        helloworld = docker.RegistryImage("helloworld", build=docker.RegistryImageBuildArgs(
            context=f"{path['cwd']}/absolutePathToContextFolder",
        ))
        ```

        <!-- schema generated by tfplugindocs -->
        ## Schema

        ### Required

        - **name** (String) The name of the Docker image.

        ### Optional

        - **build** (Block List, Max: 1) Definition for building the image (see below for nested schema)
        - **id** (String) The ID of this resource.
        - **insecure_skip_verify** (Boolean) If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        - **keep_remotely** (Boolean) If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from the docker registry on destroy operation. Defaults to `false`

        ### Read-Only

        - **sha256_digest** (String) The sha256 digest of the image.

        <a id="nestedblock--build"></a>
        ### Nested Schema for `build`

        Required:

        - **context** (String) The absolute path to the context folder. You can use the helper function '${path.cwd}/context-dir'.

        Optional:

        - **auth_config** (Block List) The configuration for the authentication (see below for nested schema)
        - **build_args** (Map of String) Pairs for build-time variables in the form TODO
        - **build_id** (String) BuildID is an optional identifier that can be passed together with the build request. The
        - **cache_from** (List of String) Images to consider as cache sources
        - **cgroup_parent** (String) Optional parent cgroup for the container
        - **cpu_period** (Number) The length of a CPU period in microseconds
        - **cpu_quota** (Number) Microseconds of CPU time that the container can get in a CPU period
        - **cpu_set_cpus** (String) CPUs in which to allow execution (e.g., `0-3`, `0`, `1`)
        - **cpu_set_mems** (String) MEMs in which to allow execution (`0-3`, `0`, `1`)
        - **cpu_shares** (Number) CPU shares (relative weight)
        - **dockerfile** (String) Dockerfile file. Defaults to `Dockerfile`
        - **extra_hosts** (List of String) A list of hostnames/IP mappings to add to the container’s /etc/hosts file. Specified in the form ["hostname:IP"]
        - **force_remove** (Boolean) Always remove intermediate containers
        - **isolation** (String) Isolation represents the isolation technology of a container. The supported values are
        - **labels** (Map of String) User-defined key/value metadata
        - **memory** (Number) Set memory limit for build
        - **memory_swap** (Number) Total memory (memory + swap), -1 to enable unlimited swap
        - **network_mode** (String) Set the networking mode for the RUN instructions during build
        - **no_cache** (Boolean) Do not use the cache when building the image
        - **platform** (String) Set platform if server is multi-platform capable
        - **pull_parent** (Boolean) Attempt to pull the image even if an older image exists locally
        - **remote_context** (String) A Git repository URI or HTTP/HTTPS context URI
        - **remove** (Boolean) Remove intermediate containers after a successful build (default behavior)
        - **security_opt** (List of String) The security options
        - **session_id** (String) Set an ID for the build session
        - **shm_size** (Number) Size of /dev/shm in bytes. The size must be greater than 0
        - **squash** (Boolean) If true the new layers are squashed into a new image with a single new layer
        - **suppress_output** (Boolean) Suppress the build output and print image ID on success
        - **target** (String) Set the target build stage to build
        - **ulimit** (Block List) Configuration for ulimits (see below for nested schema)
        - **version** (String) Version of the unerlying builder to use

        <a id="nestedblock--build--auth_config"></a>
        ### Nested Schema for `build.auth_config`

        Required:

        - **host_name** (String) hostname of the registry

        Optional:

        - **auth** (String) the auth token
        - **email** (String) the user emal
        - **identity_token** (String) the identity token
        - **password** (String) the registry password
        - **registry_token** (String) the registry token
        - **server_address** (String) the server address
        - **user_name** (String) the registry user name

        <a id="nestedblock--build--ulimit"></a>
        ### Nested Schema for `build.ulimit`

        Required:

        - **hard** (Number) soft limit
        - **name** (String) type of ulimit, e.g. `nofile`
        - **soft** (Number) hard limit

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RegistryImageBuildArgs']] build: Definition for building the image
        :param pulumi.Input[bool] insecure_skip_verify: If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        :param pulumi.Input[bool] keep_remotely: If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from
               the docker registry on destroy operation. Defaults to `false`
        :param pulumi.Input[str] name: The name of the Docker image.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[RegistryImageArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        <!-- Bug: Type and Name are switched -->
        Manages the lifecycle of docker image/tag in a registry.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_docker as docker

        helloworld = docker.RegistryImage("helloworld", build=docker.RegistryImageBuildArgs(
            context=f"{path['cwd']}/absolutePathToContextFolder",
        ))
        ```

        <!-- schema generated by tfplugindocs -->
        ## Schema

        ### Required

        - **name** (String) The name of the Docker image.

        ### Optional

        - **build** (Block List, Max: 1) Definition for building the image (see below for nested schema)
        - **id** (String) The ID of this resource.
        - **insecure_skip_verify** (Boolean) If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        - **keep_remotely** (Boolean) If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from the docker registry on destroy operation. Defaults to `false`

        ### Read-Only

        - **sha256_digest** (String) The sha256 digest of the image.

        <a id="nestedblock--build"></a>
        ### Nested Schema for `build`

        Required:

        - **context** (String) The absolute path to the context folder. You can use the helper function '${path.cwd}/context-dir'.

        Optional:

        - **auth_config** (Block List) The configuration for the authentication (see below for nested schema)
        - **build_args** (Map of String) Pairs for build-time variables in the form TODO
        - **build_id** (String) BuildID is an optional identifier that can be passed together with the build request. The
        - **cache_from** (List of String) Images to consider as cache sources
        - **cgroup_parent** (String) Optional parent cgroup for the container
        - **cpu_period** (Number) The length of a CPU period in microseconds
        - **cpu_quota** (Number) Microseconds of CPU time that the container can get in a CPU period
        - **cpu_set_cpus** (String) CPUs in which to allow execution (e.g., `0-3`, `0`, `1`)
        - **cpu_set_mems** (String) MEMs in which to allow execution (`0-3`, `0`, `1`)
        - **cpu_shares** (Number) CPU shares (relative weight)
        - **dockerfile** (String) Dockerfile file. Defaults to `Dockerfile`
        - **extra_hosts** (List of String) A list of hostnames/IP mappings to add to the container’s /etc/hosts file. Specified in the form ["hostname:IP"]
        - **force_remove** (Boolean) Always remove intermediate containers
        - **isolation** (String) Isolation represents the isolation technology of a container. The supported values are
        - **labels** (Map of String) User-defined key/value metadata
        - **memory** (Number) Set memory limit for build
        - **memory_swap** (Number) Total memory (memory + swap), -1 to enable unlimited swap
        - **network_mode** (String) Set the networking mode for the RUN instructions during build
        - **no_cache** (Boolean) Do not use the cache when building the image
        - **platform** (String) Set platform if server is multi-platform capable
        - **pull_parent** (Boolean) Attempt to pull the image even if an older image exists locally
        - **remote_context** (String) A Git repository URI or HTTP/HTTPS context URI
        - **remove** (Boolean) Remove intermediate containers after a successful build (default behavior)
        - **security_opt** (List of String) The security options
        - **session_id** (String) Set an ID for the build session
        - **shm_size** (Number) Size of /dev/shm in bytes. The size must be greater than 0
        - **squash** (Boolean) If true the new layers are squashed into a new image with a single new layer
        - **suppress_output** (Boolean) Suppress the build output and print image ID on success
        - **target** (String) Set the target build stage to build
        - **ulimit** (Block List) Configuration for ulimits (see below for nested schema)
        - **version** (String) Version of the unerlying builder to use

        <a id="nestedblock--build--auth_config"></a>
        ### Nested Schema for `build.auth_config`

        Required:

        - **host_name** (String) hostname of the registry

        Optional:

        - **auth** (String) the auth token
        - **email** (String) the user emal
        - **identity_token** (String) the identity token
        - **password** (String) the registry password
        - **registry_token** (String) the registry token
        - **server_address** (String) the server address
        - **user_name** (String) the registry user name

        <a id="nestedblock--build--ulimit"></a>
        ### Nested Schema for `build.ulimit`

        Required:

        - **hard** (Number) soft limit
        - **name** (String) type of ulimit, e.g. `nofile`
        - **soft** (Number) hard limit

        :param str resource_name: The name of the resource.
        :param RegistryImageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegistryImageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 build: Optional[pulumi.Input[pulumi.InputType['RegistryImageBuildArgs']]] = None,
                 insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
                 keep_remotely: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegistryImageArgs.__new__(RegistryImageArgs)

            __props__.__dict__["build"] = build
            __props__.__dict__["insecure_skip_verify"] = insecure_skip_verify
            __props__.__dict__["keep_remotely"] = keep_remotely
            __props__.__dict__["name"] = name
            __props__.__dict__["sha256_digest"] = None
        super(RegistryImage, __self__).__init__(
            'docker:index/registryImage:RegistryImage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            build: Optional[pulumi.Input[pulumi.InputType['RegistryImageBuildArgs']]] = None,
            insecure_skip_verify: Optional[pulumi.Input[bool]] = None,
            keep_remotely: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            sha256_digest: Optional[pulumi.Input[str]] = None) -> 'RegistryImage':
        """
        Get an existing RegistryImage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['RegistryImageBuildArgs']] build: Definition for building the image
        :param pulumi.Input[bool] insecure_skip_verify: If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        :param pulumi.Input[bool] keep_remotely: If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from
               the docker registry on destroy operation. Defaults to `false`
        :param pulumi.Input[str] name: The name of the Docker image.
        :param pulumi.Input[str] sha256_digest: The sha256 digest of the image.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RegistryImageState.__new__(_RegistryImageState)

        __props__.__dict__["build"] = build
        __props__.__dict__["insecure_skip_verify"] = insecure_skip_verify
        __props__.__dict__["keep_remotely"] = keep_remotely
        __props__.__dict__["name"] = name
        __props__.__dict__["sha256_digest"] = sha256_digest
        return RegistryImage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def build(self) -> pulumi.Output[Optional['outputs.RegistryImageBuild']]:
        """
        Definition for building the image
        """
        return pulumi.get(self, "build")

    @property
    @pulumi.getter(name="insecureSkipVerify")
    def insecure_skip_verify(self) -> pulumi.Output[Optional[bool]]:
        """
        If `true`, the verification of TLS certificates of the server/registry is disabled. Defaults to `false`
        """
        return pulumi.get(self, "insecure_skip_verify")

    @property
    @pulumi.getter(name="keepRemotely")
    def keep_remotely(self) -> pulumi.Output[Optional[bool]]:
        """
        If true, then the Docker image won't be deleted on destroy operation. If this is false, it will delete the image from
        the docker registry on destroy operation. Defaults to `false`
        """
        return pulumi.get(self, "keep_remotely")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Docker image.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sha256Digest")
    def sha256_digest(self) -> pulumi.Output[str]:
        """
        The sha256 digest of the image.
        """
        return pulumi.get(self, "sha256_digest")

