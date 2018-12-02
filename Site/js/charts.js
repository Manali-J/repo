

AmCharts.makeChart("chartdiv",
{
    "type": "xy",
    "autoMarginOffset": 40,
    "marginRight": 60,
    "marginTop": 60,
    "startDuration": 1.5,
    "fontSize": 13,
    "handDrawn": true,
    "theme": "default",
    "trendLines": [],
    "graphs": [
        {
            "balloonText": "x:<b>[[x]]</b> y:<b>[[y]]</b><br>value:<b>[[value]]</b>",
            "bullet": "diamond",
            "bulletBorderThickness": 0,
            "id": "AmGraph-1",
            "lineAlpha": 0,
            "lineColor": "#b0de09",
            "maxBulletSize": 130,
            "minBulletSize": 5,
            "periodSpan": 0,
            "valueField": "value",
            "xField": "x",
            "yField": "y"
        },
        {
            "balloonText": "x:<b>[[x]]</b> y:<b>[[y]]</b><br>value:<b>[[value]]</b>",
            "bullet": "round",
            "id": "AmGraph-2",
            "lineAlpha": 0,
            "lineColor": "#fcd202",
            "maxBulletSize": 130,
            "minBulletSize": 5,
            "valueField": "value2",
            "xField": "x2",
            "yField": "y2"
        }
    ],
    "guides": [],
    "valueAxes": [
        {
            "id": "ValueAxis-1",
            "axisAlpha": 0
        },
        {
            "id": "ValueAxis-2",
            "position": "bottom",
            "axisAlpha": 0
        }
    ],
    "allLabels": [],
    "balloon": {},
    "titles": [],
    "dataProvider": [
        {
            "y": 10,
            "x": 14,
            "value": 59,
            "y2": -5,
            "x2": -3,
            "value2": 44
        },
        {
            "y": 5,
            "x": 3,
            "value": 50,
            "y2": -15,
            "x2": -8,
            "value2": 12
        },
        {
            "y": -10,
            "x": -3,
            "value": 19,
            "y2": "5",
            "x2": 6,
            "value2": 35
        },
        {
            "y": -6,
            "x": 5,
            "value": 65,
            "y2": "5",
            "x2": "9",
            "value2": 168
        },
        {
            "y": 15,
            "x": -4,
            "value": 92,
            "y2": -10,
            "x2": -8,
            "value2": 102
        },
        {
            "y": 13,
            "x": 1,
            "value": 8,
            "y2": "3",
            "x2": -3,
            "value2": 41
        },
        {
            "y": 1,
            "x": 6,
            "value": 35,
            "y2": 0,
            "x2": -3,
            "value2": 16
        }
    ]
}
);
