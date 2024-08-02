function buildBarChart(chartData) {

    // look through crime offenses, group and count them 
    let groupedCrimes = chartData.reduce((acc, str) => {
        if (!acc[str]) {
            acc[str] = 0;
        }
        acc[str]++;
        return acc;
    }, {});

    let labels = Object.keys(groupedCrimes);
    let counts = Object.values(groupedCrimes);

    // rename the crime offenses
    const labelMapping = {
    "THEFT F/AUTO": "Car Break-In",
    "THEFT/OTHER": "Theft",
    "ROBBERY": "Armed Robbery",
    "MOTOR VEHICLE THEFT": "Auto Theft",
    "SEX ABUSE": "Sex Abuse",
    "ASSAULT W/DANGEROUS WEAPON": "Assault",
    "HOMICIDE": "Homicide",
    "BURGLARY": "Burglary",
    'ARSON': 'Arson'
    };

    labels = labels.map(label => labelMapping[label] || label);


    // plot the crime offenses as a horizontal bar chart
    var trace1 = {
        x: counts,
        y: labels,
        name: 'Crime Types',
        type: 'bar',
        orientation: 'h',
        marker: {
            color: 'rgba(157,167,86,0.8)',
            width: 1
        },
        hovertemplate: 'Crime Count: %{x}<br>Crime Type: %{y}<extra></extra>'
    };

    var data = [trace1];

    var layout = {
        title: 'Amount of Crime by Type',
        xaxis: {
            title: 'Crime Count',
        },
        yaxis: {
            automargin: true,
            // Add a margin on the left side to accommodate longer labels
            margin: {
                l: 300 // Adjust this value according to your preference
            }
        },
        font: {
            family: 'Arial',  // Specify the font family
            size: 12,         // Specify the font size
            color: 'black'    // Specify the font color
        }
    };

    Plotly.newPlot('myDiv', data, layout);
};



// counts collected for temp ranges
let tempRanges = ['15-19','20-24', '25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80-84','85-89','90-95'];
let crimeCounts = [51, 0,127,724,1667,2167,2818,2435,2432,2789,2562,3132,2743,1622,1452,356];


// plot the counts per temp range
let trace2 = {
x: tempRanges,
y: crimeCounts,
type: 'bar',
marker: {
    color: 'rgba(95, 91, 91,0.8)',
    width: 1    
},
hovertemplate: 'Temperature: %{customdata}F°<br>Crime Count: %{y}<extra></extra>',
customdata: tempRanges

};

let data2 = [trace2];

let layout2 = {
title: 'Crime Counts by Temperature',
xaxis: {
    title: 'Temperature (°F)', 
    ticktext: [15, 35, 55, 75, 95],
    tickvals: [0,4,8,12,15]
},
yaxis: {
    title: 'Crime Count'
},
font: {
    family: 'Arial',  // Specify the font family
    size: 12,         // Specify the font size
    color: 'black'    // Specify the font color
},
bargap: 0
};

Plotly.newPlot('myChart', data2, layout2);


