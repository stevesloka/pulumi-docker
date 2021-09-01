// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Inputs
{

    public sealed class ServiceTaskSpecContainerSpecDnsConfigGetArgs : Pulumi.ResourceArgs
    {
        [Input("nameservers", required: true)]
        private InputList<string>? _nameservers;
        public InputList<string> Nameservers
        {
            get => _nameservers ?? (_nameservers = new InputList<string>());
            set => _nameservers = value;
        }

        [Input("options")]
        private InputList<string>? _options;
        public InputList<string> Options
        {
            get => _options ?? (_options = new InputList<string>());
            set => _options = value;
        }

        [Input("searches")]
        private InputList<string>? _searches;
        public InputList<string> Searches
        {
            get => _searches ?? (_searches = new InputList<string>());
            set => _searches = value;
        }

        public ServiceTaskSpecContainerSpecDnsConfigGetArgs()
        {
        }
    }
}
