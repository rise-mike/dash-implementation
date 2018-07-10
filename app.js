var chartApp = angular.module('chartApp', ['ngRoute']);

chartApp.config(function ($routeProvider) {
  $routeProvider
  .when('/', {
    templateUrl: 'views/chart.html',
    controller: 'projectController'
  })
  .when('/projects', {
    templateUrl: 'views/all_projects.html',
    controller: "projectController"
  })
  .when('/specialists', {
    templateUrl: 'views/specialists.html',
    controller: 'projectController'
  })
});

chartApp.controller('chartController', ['$scope', '$http', function($scope, $http) {

//   $scope.chartData = {}

//   $http.get('chart/list.json').success(function(response) {
//     console.log("RESPONSE: ", response)
//     $scope.chartData = response
//   })
// console.log("On the scope ", $scope.chartData)

}])

chartApp.controller('projectController', ['$scope', '$http', function($scope, $http) {

  $scope.projects = []
  
  $http.get('chart/output.json').success(function(response) {
    $scope.projects = response
  })

  $scope.getWidth = function(project){
    elementVal = String(project.progress) + "%"
    return elementVal
  }

}])

chartApp.controller('specialistController', ['$scope', '$http', function($scope, $http) {

}])