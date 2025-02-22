// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Inputs
{

    public sealed class ServiceEndpointSpecPortGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Name of the service
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        [Input("publishMode")]
        public Input<string>? PublishMode { get; set; }

        [Input("publishedPort")]
        public Input<int>? PublishedPort { get; set; }

        [Input("targetPort", required: true)]
        public Input<int> TargetPort { get; set; } = null!;

        public ServiceEndpointSpecPortGetArgs()
        {
        }
    }
}
