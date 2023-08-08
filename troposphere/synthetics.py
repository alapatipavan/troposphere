# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, integer
from .validators.synthetics import canary_runtime_version


class S3Encryption(AWSProperty):
    """
    `S3Encryption <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-s3encryption.html>`__
    """

    props: PropsDictType = {
        "EncryptionMode": (str, False),
        "KmsKeyArn": (str, False),
    }


class ArtifactConfig(AWSProperty):
    """
    `ArtifactConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-artifactconfig.html>`__
    """

    props: PropsDictType = {
        "S3Encryption": (S3Encryption, False),
    }


class Code(AWSProperty):
    """
    `Code <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-code.html>`__
    """

    props: PropsDictType = {
        "Handler": (str, True),
        "S3Bucket": (str, False),
        "S3Key": (str, False),
        "S3ObjectVersion": (str, False),
        "Script": (str, False),
        "SourceLocationArn": (str, False),
    }


class RunConfig(AWSProperty):
    """
    `RunConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-runconfig.html>`__
    """

    props: PropsDictType = {
        "ActiveTracing": (boolean, False),
        "EnvironmentVariables": (dict, False),
        "MemoryInMB": (integer, False),
        "TimeoutInSeconds": (integer, False),
    }


class Schedule(AWSProperty):
    """
    `Schedule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-schedule.html>`__
    """

    props: PropsDictType = {
        "DurationInSeconds": (str, False),
        "Expression": (str, True),
    }


class VPCConfig(AWSProperty):
    """
    `VPCConfig <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-vpcconfig.html>`__
    """

    props: PropsDictType = {
        "SecurityGroupIds": ([str], True),
        "SubnetIds": ([str], True),
        "VpcId": (str, False),
    }


class BaseScreenshot(AWSProperty):
    """
    `BaseScreenshot <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-basescreenshot.html>`__
    """

    props: PropsDictType = {
        "IgnoreCoordinates": ([str], False),
        "ScreenshotName": (str, True),
    }


class VisualReference(AWSProperty):
    """
    `VisualReference <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-synthetics-canary-visualreference.html>`__
    """

    props: PropsDictType = {
        "BaseCanaryRunId": (str, True),
        "BaseScreenshots": ([BaseScreenshot], False),
    }


class Canary(AWSObject):
    """
    `Canary <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html>`__
    """

    resource_type = "AWS::Synthetics::Canary"

    props: PropsDictType = {
        "ArtifactConfig": (ArtifactConfig, False),
        "ArtifactS3Location": (str, True),
        "Code": (Code, True),
        "ExecutionRoleArn": (str, True),
        "FailureRetentionPeriod": (integer, False),
        "Name": (str, True),
        "RunConfig": (RunConfig, False),
        "RuntimeVersion": (canary_runtime_version, True),
        "Schedule": (Schedule, True),
        "StartCanaryAfterCreation": (boolean, False),
        "SuccessRetentionPeriod": (integer, False),
        "Tags": (Tags, False),
        "VPCConfig": (VPCConfig, False),
        "VisualReference": (VisualReference, False),
    }


class Group(AWSObject):
    """
    `Group <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-group.html>`__
    """

    resource_type = "AWS::Synthetics::Group"

    props: PropsDictType = {
        "Name": (str, True),
        "ResourceArns": ([str], False),
        "Tags": (Tags, False),
    }
