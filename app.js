var chartApp = angular.module('chartApp', ['ngRoute']);

chartApp.config(function ($routeProvider) {
  $routeProvider
  .when('/', {
    templateUrl: 'views/dash.html',
    controller: 'projectController'
  })
  .when('/dash', {
    templateUrl: 'views/dash.html',
    controller: 'dashController'
  })
  // .when('/chart', {
  //   templateUrl: 'views/chart.html',
  //   controller: 'chartController'
  // })
  .when('/projects', {
    templateUrl: 'views/all_projects.html',
    controller: "projectController"
  })
  .when('/report', {
    templateUrl: 'views/report.html',
    controller: "projectController"
  })
});

// chartApp.controller('chartController', ['$scope', '$http', function($scope, $http) {

//   $scope.chartData = {}

//   $http.get('chart/list.json').success(function(response) {
//     console.log("RESPONSE: ", response)
//     $scope.chartData = response
//   })
// console.log("On the scope ", $scope.chartData)

// }])

chartApp.controller('dashController', ['$scope', '$http', function($scope, $http) {

  $scope.projects = []
  $scope.specialists = ['ariel.png', 'bhuvi.png', 'dhiraj.png', 'ed.png', 'maulin.png']
  
  $http.get('data/projects.json').success(function(response) {
    $scope.projects = response
  })

  $scope.getWidth = function(project){
    elementVal = String(project.progress) + "%"
    return elementVal
  }


}])

chartApp.controller('projectController', ['$scope', '$http', function($scope, $http) {

  $scope.projects = []
  
  $http.get('data/projects.json').success(function(response) {
    $scope.projects = response
  })

  $scope.getWidth = function(project){
    elementVal = String(project.progress) + "%"
    return elementVal
  }

}])