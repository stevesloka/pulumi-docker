// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Docker.Inputs
{

    public sealed class RemoteImageBuildGetArgs : Pulumi.ResourceArgs
    {
        [Input("buildArg")]
        private InputMap<string>? _buildArg;

        /// <summary>
        /// Set build-time variables
        /// </summary>
        public InputMap<string> BuildArg
        {
            get => _buildArg ?? (_buildArg = new InputMap<string>());
            set => _buildArg = value;
        }

        /// <summary>
        /// Name of the Dockerfile. Defaults to `Dockerfile`.
        /// </summary>
        [Input("dockerfile")]
        public Input<string>? Dockerfile { get; set; }

        /// <summary>
        /// Always remove intermediate containers
        /// </summary>
        [Input("forceRemove")]
        public Input<bool>? ForceRemove { get; set; }

        [Input("label")]
        private InputMap<string>? _label;

        /// <summary>
        /// Set metadata for an image
        /// </summary>
        public InputMap<string> Label
        {
            get => _label ?? (_label = new InputMap<string>());
            set => _label = value;
        }

        /// <summary>
        /// Do not use cache when building the image
        /// </summary>
        [Input("noCache")]
        public Input<bool>? NoCache { get; set; }

        /// <summary>
        /// Context path
        /// </summary>
        [Input("path", required: true)]
        public Input<string> Path { get; set; } = null!;

        /// <summary>
        /// Remove intermediate containers after a successful build. Defaults to  `true`.
        /// </summary>
        [Input("remove")]
        public Input<bool>? Remove { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// Name and optionally a tag in the 'name:tag' format
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// Set the target build stage to build
        /// </summary>
        [Input("target")]
        public Input<string>? Target { get; set; }

        public RemoteImageBuildGetArgs()
        {
        }
    }
}
