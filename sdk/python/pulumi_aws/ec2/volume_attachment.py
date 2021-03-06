# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class VolumeAttachment(pulumi.CustomResource):
    device_name: pulumi.Output[str]
    """
    The device name to expose to the instance (for
    example, `/dev/sdh` or `xvdh`).  See [Device Naming on Linux Instances][1] and [Device Naming on Windows Instances][2] for more information.
    """
    force_detach: pulumi.Output[bool]
    """
    Set to `true` if you want to force the
    volume to detach. Useful if previous attempts failed, but use this option only
    as a last resort, as this can result in **data loss**. See
    [Detaching an Amazon EBS Volume from an Instance][3] for more information.
    """
    instance_id: pulumi.Output[str]
    """
    ID of the Instance to attach to
    """
    skip_destroy: pulumi.Output[bool]
    """
    Set this to true if you do not wish
    to detach the volume from the instance to which it is attached at destroy
    time, and instead just remove the attachment from Terraform state. This is
    useful when destroying an instance which has volumes created by some other
    means attached.
    """
    volume_id: pulumi.Output[str]
    """
    ID of the Volume to be attached
    """
    def __init__(__self__, resource_name, opts=None, device_name=None, force_detach=None, instance_id=None, skip_destroy=None, volume_id=None, __name__=None, __opts__=None):
        """
        Provides an AWS EBS Volume Attachment as a top level resource, to attach and
        detach volumes from AWS Instances.
        
        > **NOTE on EBS block devices:** If you use `ebs_block_device` on an `aws_instance`, Terraform will assume management over the full set of non-root EBS block devices for the instance, and treats additional block devices as drift. For this reason, `ebs_block_device` cannot be mixed with external `aws_ebs_volume` + `aws_ebs_volume_attachment` resources for a given instance.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] device_name: The device name to expose to the instance (for
               example, `/dev/sdh` or `xvdh`).  See [Device Naming on Linux Instances][1] and [Device Naming on Windows Instances][2] for more information.
        :param pulumi.Input[bool] force_detach: Set to `true` if you want to force the
               volume to detach. Useful if previous attempts failed, but use this option only
               as a last resort, as this can result in **data loss**. See
               [Detaching an Amazon EBS Volume from an Instance][3] for more information.
        :param pulumi.Input[str] instance_id: ID of the Instance to attach to
        :param pulumi.Input[bool] skip_destroy: Set this to true if you do not wish
               to detach the volume from the instance to which it is attached at destroy
               time, and instead just remove the attachment from Terraform state. This is
               useful when destroying an instance which has volumes created by some other
               means attached.
        :param pulumi.Input[str] volume_id: ID of the Volume to be attached
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if device_name is None:
            raise TypeError("Missing required property 'device_name'")
        __props__['device_name'] = device_name

        __props__['force_detach'] = force_detach

        if instance_id is None:
            raise TypeError("Missing required property 'instance_id'")
        __props__['instance_id'] = instance_id

        __props__['skip_destroy'] = skip_destroy

        if volume_id is None:
            raise TypeError("Missing required property 'volume_id'")
        __props__['volume_id'] = volume_id

        super(VolumeAttachment, __self__).__init__(
            'aws:ec2/volumeAttachment:VolumeAttachment',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

