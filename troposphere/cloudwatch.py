# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean, double, integer
from .validators.cloudwatch import (
    dict_or_string,
    validate_alarm,
    validate_dashboard,
    validate_treat_missing_data,
    validate_unit,
)


class MetricDimension(AWSProperty):
    """
    `MetricDimension <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-alarm-dimension.html>`__
    """

    props: PropsDictType = {
        "Name": (str, True),
        "Value": (str, True),
    }


class Metric(AWSProperty):
    """
    `Metric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metric.html>`__
    """

    props: PropsDictType = {
        "Dimensions": ([MetricDimension], False),
        "MetricName": (str, True),
        "Namespace": (str, True),
    }


class MetricStat(AWSProperty):
    """
    `MetricStat <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricstat.html>`__
    """

    props: PropsDictType = {
        "Metric": (Metric, True),
        "Period": (integer, True),
        "Stat": (str, True),
        "Unit": (validate_unit, False),
    }


class MetricDataQuery(AWSProperty):
    """
    `MetricDataQuery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricdataquery.html>`__
    """

    props: PropsDictType = {
        "AccountId": (str, False),
        "Expression": (str, False),
        "Id": (str, True),
        "Label": (str, False),
        "MetricStat": (MetricStat, False),
        "Period": (integer, False),
        "ReturnData": (boolean, False),
    }


class Alarm(AWSObject):
    """
    `Alarm <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-alarm.html>`__
    """

    resource_type = "AWS::CloudWatch::Alarm"

    props: PropsDictType = {
        "ActionsEnabled": (boolean, False),
        "AlarmActions": ([str], False),
        "AlarmDescription": (str, False),
        "AlarmName": (str, False),
        "ComparisonOperator": (str, True),
        "DatapointsToAlarm": (integer, False),
        "Dimensions": ([MetricDimension], False),
        "EvaluateLowSampleCountPercentile": (str, False),
        "EvaluationPeriods": (integer, True),
        "ExtendedStatistic": (str, False),
        "InsufficientDataActions": ([str], False),
        "MetricName": (str, False),
        "Metrics": ([MetricDataQuery], False),
        "Namespace": (str, False),
        "OKActions": ([str], False),
        "Period": (integer, False),
        "Statistic": (str, False),
        "Tags": (Tags, False),
        "Threshold": (double, False),
        "ThresholdMetricId": (str, False),
        "TreatMissingData": (validate_treat_missing_data, False),
        "Unit": (str, False),
    }

    def validate(self):
        validate_alarm(self)


class Range(AWSProperty):
    """
    `Range <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-range.html>`__
    """

    props: PropsDictType = {
        "EndTime": (str, True),
        "StartTime": (str, True),
    }


class Configuration(AWSProperty):
    """
    `Configuration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-configuration.html>`__
    """

    props: PropsDictType = {
        "ExcludedTimeRanges": ([Range], False),
        "MetricTimeZone": (str, False),
    }


class MetricMathAnomalyDetector(AWSProperty):
    """
    `MetricMathAnomalyDetector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-metricmathanomalydetector.html>`__
    """

    props: PropsDictType = {
        "MetricDataQueries": ([MetricDataQuery], False),
    }


class SingleMetricAnomalyDetector(AWSProperty):
    """
    `SingleMetricAnomalyDetector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-anomalydetector-singlemetricanomalydetector.html>`__
    """

    props: PropsDictType = {
        "AccountId": (str, False),
        "Dimensions": ([MetricDimension], False),
        "MetricName": (str, False),
        "Namespace": (str, False),
        "Stat": (str, False),
    }


class AnomalyDetector(AWSObject):
    """
    `AnomalyDetector <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-anomalydetector.html>`__
    """

    resource_type = "AWS::CloudWatch::AnomalyDetector"

    props: PropsDictType = {
        "Configuration": (Configuration, False),
        "Dimensions": ([MetricDimension], False),
        "MetricMathAnomalyDetector": (MetricMathAnomalyDetector, False),
        "MetricName": (str, False),
        "Namespace": (str, False),
        "SingleMetricAnomalyDetector": (SingleMetricAnomalyDetector, False),
        "Stat": (str, False),
    }


class CompositeAlarm(AWSObject):
    """
    `CompositeAlarm <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-compositealarm.html>`__
    """

    resource_type = "AWS::CloudWatch::CompositeAlarm"

    props: PropsDictType = {
        "ActionsEnabled": (boolean, False),
        "ActionsSuppressor": (str, False),
        "ActionsSuppressorExtensionPeriod": (integer, False),
        "ActionsSuppressorWaitPeriod": (integer, False),
        "AlarmActions": ([str], False),
        "AlarmDescription": (str, False),
        "AlarmName": (str, False),
        "AlarmRule": (str, True),
        "InsufficientDataActions": ([str], False),
        "OKActions": ([str], False),
        "Tags": (Tags, False),
    }


class Dashboard(AWSObject):
    """
    `Dashboard <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-dashboard.html>`__
    """

    resource_type = "AWS::CloudWatch::Dashboard"

    props: PropsDictType = {
        "DashboardBody": (dict_or_string, True),
        "DashboardName": (str, False),
    }

    def validate(self):
        validate_dashboard(self)


class InsightRule(AWSObject):
    """
    `InsightRule <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-insightrule.html>`__
    """

    resource_type = "AWS::CloudWatch::InsightRule"

    props: PropsDictType = {
        "RuleBody": (str, True),
        "RuleName": (str, True),
        "RuleState": (str, True),
        "Tags": (Tags, False),
    }


class MetricStreamFilter(AWSProperty):
    """
    `MetricStreamFilter <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamfilter.html>`__
    """

    props: PropsDictType = {
        "MetricNames": ([str], False),
        "Namespace": (str, True),
    }


class MetricStreamStatisticsMetric(AWSProperty):
    """
    `MetricStreamStatisticsMetric <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsmetric.html>`__
    """

    props: PropsDictType = {
        "MetricName": (str, True),
        "Namespace": (str, True),
    }


class MetricStreamStatisticsConfiguration(AWSProperty):
    """
    `MetricStreamStatisticsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudwatch-metricstream-metricstreamstatisticsconfiguration.html>`__
    """

    props: PropsDictType = {
        "AdditionalStatistics": ([str], True),
        "IncludeMetrics": ([MetricStreamStatisticsMetric], True),
    }


class MetricStream(AWSObject):
    """
    `MetricStream <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cloudwatch-metricstream.html>`__
    """

    resource_type = "AWS::CloudWatch::MetricStream"

    props: PropsDictType = {
        "ExcludeFilters": ([MetricStreamFilter], False),
        "FirehoseArn": (str, True),
        "IncludeFilters": ([MetricStreamFilter], False),
        "IncludeLinkedAccountsMetrics": (boolean, False),
        "Name": (str, False),
        "OutputFormat": (str, True),
        "RoleArn": (str, True),
        "StatisticsConfigurations": ([MetricStreamStatisticsConfiguration], False),
        "Tags": (Tags, False),
    }
