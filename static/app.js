'use strict'

var myApp = angular.module("myApp", [
	"ngRoute",
	"App"

])

myApp.config(['$routeProvider', function($routeProvider) {
  $routeProvider
  .when('/', {
    templateUrl: 'static/partials/first.html',
    controller: "uploadController"
  })
  .when('/orders', {
    templateUrl: 'static/partials/orders.html',
    controller: "ordersController"
  })  
  .when('/orderbyId', {
    templateUrl: 'static/partials/orderbyId.html',
    controller: "orderbyIdController"
  })    
  .otherwise({
    redirectTo: '/'
  });
}]);   

var App = angular.module('App',[]);

