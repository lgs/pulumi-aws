# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Model(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) assigned by AWS to this model.
    """
    containers: pulumi.Output[list]
    """
    Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
    """
    enable_network_isolation: pulumi.Output[bool]
    """
    Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
    """
    execution_role_arn: pulumi.Output[str]
    """
    A role that SageMaker can assume to access model artifacts and docker images for deployment.
    """
    name: pulumi.Output[str]
    """
    The name of the model (must be unique). If omitted, Terraform will assign a random, unique name.
    """
    primary_container: pulumi.Output[dict]
    """
    The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    vpc_config: pulumi.Output[dict]
    """
    Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
    """
    def __init__(__self__, __name__, __opts__=None, containers=None, enable_network_isolation=None, execution_role_arn=None, name=None, primary_container=None, tags=None, vpc_config=None):
        """
        Provides a SageMaker model resource.
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] containers: Specifies containers in the inference pipeline. If not specified, the `primary_container` argument is required. Fields are documented below.
        :param pulumi.Input[bool] enable_network_isolation: Isolates the model container. No inbound or outbound network calls can be made to or from the model container.
        :param pulumi.Input[str] execution_role_arn: A role that SageMaker can assume to access model artifacts and docker images for deployment.
        :param pulumi.Input[str] name: The name of the model (must be unique). If omitted, Terraform will assign a random, unique name.
        :param pulumi.Input[dict] primary_container: The primary docker image containing inference code that is used when the model is deployed for predictions.  If not specified, the `container` argument is required. Fields are documented below.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        :param pulumi.Input[dict] vpc_config: Specifies the VPC that you want your model to connect to. VpcConfig is used in hosting services and in batch transform.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['containers'] = containers

        __props__['enable_network_isolation'] = enable_network_isolation

        if not execution_role_arn:
            raise TypeError('Missing required property execution_role_arn')
        __props__['execution_role_arn'] = execution_role_arn

        __props__['name'] = name

        __props__['primary_container'] = primary_container

        __props__['tags'] = tags

        __props__['vpc_config'] = vpc_config

        __props__['arn'] = None

        super(Model, __self__).__init__(
            'aws:sagemaker/model:Model',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
