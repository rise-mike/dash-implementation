// const requirejs = require('require.js')

const chartData = require('list.js')

google.charts.load('current', {'packages':['gantt']});
google.charts.setOnLoadCallback(drawChart);

console.log("CHART! Woo :  ", chartData)

function drawChart() {

  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Task ID');
  data.addColumn('string', 'Task Name');
  data.addColumn('string', 'Resource');
  data.addColumn('date', 'Start Date');
  data.addColumn('date', 'End Date');
  data.addColumn('number', 'Duration');
  data.addColumn('number', 'Percent Complete');
  data.addColumn('string', 'Dependencies');

  data.addRows([
    ['2014Spring', 'Clio', 'Maulin',
      new Date(2018, 4, 22), new Date(2018, 6, 18), null, 80, null],
    ['2014Summer', 'Pilot Coffee', 'Bhuvi',
      new Date(2018, 3, 21), new Date(2018, 5, 20), null, 80, null],
    ['2014Autumn', 'Eventbase', 'Ed',
      new Date(2018, 5, 10), new Date(2018, 6, 20), null, 90, null],
    ['2014Winter', 'Hazel', 'Ariel',
      new Date(2018, 11, 1), new Date(2018, 12, 21), null, 100, null],
    ['2015Spring', 'Profit Inc.', 'Shelby',
      new Date(2018, 2, 22), new Date(2018, 5, 20), null, 90, null],
    ['2015Summer', 'Synergy Corp LLC.', 'Dhiraj',
      new Date(2018, 5, 21), new Date(2018, 8, 20), null, 0, null],
    ['2015Autumn', 'SpaceX', 'Maulin',
      new Date(2018, 8, 21), new Date(2018, 11, 20), null, 0, null],
    ['2015Winter', 'ULA', 'Ed',
      new Date(2018, 11, 21), new Date(2018, 12, 21), null, 0, null],
    ['Football', 'Nemsis Coffee', 'Bhuvi',
      new Date(2018, 8, 4), new Date(2018, 9, 10), null, 100, null],
    ['Baseball', 'The Business Factory', 'Ariel',
      new Date(2018, 7, 31), new Date(2018, 9, 20), null, 0, null],
    ['Basketball', 'Dialpad', 'Shelby',
      new Date(2018, 6, 28), new Date(2018, 8, 20), null, 0, null],
    ['Hockey', 'Barber & Co.', 'Ed',
      new Date(2018, 9, 8), new Date(2018, 12, 21), null, 0, null]
  ]);

  var options = {
    title: "Schedule",
    height: 520,
    gantt: {
      trackHeight: 40
    }
  };

  var chart = new google.visualization.Gantt(document.getElementById('chart_div'));

  chart.draw(data, options);
}