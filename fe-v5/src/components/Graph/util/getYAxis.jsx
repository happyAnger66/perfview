import _ from 'lodash';

export default function getYAxis(yAxis, graphConfig) {
  const { threshold, yAxisMin, yAxisMax } = graphConfig;
  const newYAxis = _.clone(yAxis);
  if (threshold !== undefined && threshold !== null) {
    newYAxis.plotLines = [
      {
        value: threshold,
        color: 'red',
      },
    ];
  } else {
    delete newYAxis.plotLines;
  }

  if (graphConfig.yAxis && graphConfig.yAxis.plotLines !== undefined && graphConfig.yAxis.plotLines !== null) {
    newYAxis.plotLines = graphConfig.yAxis.plotLines;
  } else {
    delete newYAxis.plotLines;
  }

  if (yAxisMin !== undefined && yAxisMin !== null && yAxisMax !== undefined && yAxisMax !== null) {
    newYAxis.min = yAxisMin;
    newYAxis.max = yAxisMax;
  } else {
    delete newYAxis.min;
    delete newYAxis.max;
  }
  return newYAxis;
}
