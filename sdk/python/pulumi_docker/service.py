# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Service']


class Service(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth: Optional[pulumi.Input[pulumi.InputType['ServiceAuthArgs']]] = None,
                 converge_config: Optional[pulumi.Input[pulumi.InputType['ServiceConvergeConfigArgs']]] = None,
                 endpoint_spec: Optional[pulumi.Input[pulumi.InputType['ServiceEndpointSpecArgs']]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceLabelArgs']]]]] = None,
                 mode: Optional[pulumi.Input[pulumi.InputType['ServiceModeArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rollback_config: Optional[pulumi.Input[pulumi.InputType['ServiceRollbackConfigArgs']]] = None,
                 task_spec: Optional[pulumi.Input[pulumi.InputType['ServiceTaskSpecArgs']]] = None,
                 update_config: Optional[pulumi.Input[pulumi.InputType['ServiceUpdateConfigArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a Service resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ServiceAuthArgs']] auth: See Auth below for details.
        :param pulumi.Input[pulumi.InputType['ServiceConvergeConfigArgs']] converge_config: See Converge Config below for details.
        :param pulumi.Input[pulumi.InputType['ServiceEndpointSpecArgs']] endpoint_spec: See EndpointSpec below for details.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceLabelArgs']]]] labels: See Labels below for details.
        :param pulumi.Input[pulumi.InputType['ServiceModeArgs']] mode: See Mode below for details.
        :param pulumi.Input[str] name: The name of the Docker service.
        :param pulumi.Input[pulumi.InputType['ServiceRollbackConfigArgs']] rollback_config: See RollbackConfig below for details.
        :param pulumi.Input[pulumi.InputType['ServiceTaskSpecArgs']] task_spec: See TaskSpec below for details.
        :param pulumi.Input[pulumi.InputType['ServiceUpdateConfigArgs']] update_config: See UpdateConfig below for details.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['auth'] = auth
            __props__['converge_config'] = converge_config
            __props__['endpoint_spec'] = endpoint_spec
            __props__['labels'] = labels
            __props__['mode'] = mode
            __props__['name'] = name
            __props__['rollback_config'] = rollback_config
            if task_spec is None:
                raise TypeError("Missing required property 'task_spec'")
            __props__['task_spec'] = task_spec
            __props__['update_config'] = update_config
        super(Service, __self__).__init__(
            'docker:index/service:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            auth: Optional[pulumi.Input[pulumi.InputType['ServiceAuthArgs']]] = None,
            converge_config: Optional[pulumi.Input[pulumi.InputType['ServiceConvergeConfigArgs']]] = None,
            endpoint_spec: Optional[pulumi.Input[pulumi.InputType['ServiceEndpointSpecArgs']]] = None,
            labels: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceLabelArgs']]]]] = None,
            mode: Optional[pulumi.Input[pulumi.InputType['ServiceModeArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            rollback_config: Optional[pulumi.Input[pulumi.InputType['ServiceRollbackConfigArgs']]] = None,
            task_spec: Optional[pulumi.Input[pulumi.InputType['ServiceTaskSpecArgs']]] = None,
            update_config: Optional[pulumi.Input[pulumi.InputType['ServiceUpdateConfigArgs']]] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ServiceAuthArgs']] auth: See Auth below for details.
        :param pulumi.Input[pulumi.InputType['ServiceConvergeConfigArgs']] converge_config: See Converge Config below for details.
        :param pulumi.Input[pulumi.InputType['ServiceEndpointSpecArgs']] endpoint_spec: See EndpointSpec below for details.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServiceLabelArgs']]]] labels: See Labels below for details.
        :param pulumi.Input[pulumi.InputType['ServiceModeArgs']] mode: See Mode below for details.
        :param pulumi.Input[str] name: The name of the Docker service.
        :param pulumi.Input[pulumi.InputType['ServiceRollbackConfigArgs']] rollback_config: See RollbackConfig below for details.
        :param pulumi.Input[pulumi.InputType['ServiceTaskSpecArgs']] task_spec: See TaskSpec below for details.
        :param pulumi.Input[pulumi.InputType['ServiceUpdateConfigArgs']] update_config: See UpdateConfig below for details.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auth"] = auth
        __props__["converge_config"] = converge_config
        __props__["endpoint_spec"] = endpoint_spec
        __props__["labels"] = labels
        __props__["mode"] = mode
        __props__["name"] = name
        __props__["rollback_config"] = rollback_config
        __props__["task_spec"] = task_spec
        __props__["update_config"] = update_config
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def auth(self) -> pulumi.Output[Optional['outputs.ServiceAuth']]:
        """
        See Auth below for details.
        """
        return pulumi.get(self, "auth")

    @property
    @pulumi.getter(name="convergeConfig")
    def converge_config(self) -> pulumi.Output[Optional['outputs.ServiceConvergeConfig']]:
        """
        See Converge Config below for details.
        """
        return pulumi.get(self, "converge_config")

    @property
    @pulumi.getter(name="endpointSpec")
    def endpoint_spec(self) -> pulumi.Output['outputs.ServiceEndpointSpec']:
        """
        See EndpointSpec below for details.
        """
        return pulumi.get(self, "endpoint_spec")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Sequence['outputs.ServiceLabel']]:
        """
        See Labels below for details.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output['outputs.ServiceMode']:
        """
        See Mode below for details.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Docker service.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="rollbackConfig")
    def rollback_config(self) -> pulumi.Output[Optional['outputs.ServiceRollbackConfig']]:
        """
        See RollbackConfig below for details.
        """
        return pulumi.get(self, "rollback_config")

    @property
    @pulumi.getter(name="taskSpec")
    def task_spec(self) -> pulumi.Output['outputs.ServiceTaskSpec']:
        """
        See TaskSpec below for details.
        """
        return pulumi.get(self, "task_spec")

    @property
    @pulumi.getter(name="updateConfig")
    def update_config(self) -> pulumi.Output[Optional['outputs.ServiceUpdateConfig']]:
        """
        See UpdateConfig below for details.
        """
        return pulumi.get(self, "update_config")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

