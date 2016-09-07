App.controller('uploadController', ['$scope','$http','$location',
  function($scope,$http,$location) {
    $scope.uploadFile = function() {
        var f = document.getElementById('file').files[0]; 
        var formData = new FormData();
        formData.append('file', f);

        $http({method: 'POST', url: '/import/', data: formData, headers: {'Content-Type': undefined}, transformRequest: angular.identity})
            .success(function(data) {
                if (data.result.status == 200){
                    $location.path("/orders");
                }
                else{
                    $location.path("/errors");
                }

            })
            .error(function(data) {
                $location.path("/errors");
            });
        };        

 }]);

App.controller('ordersController', ['$scope','$http','$location',
  function($scope,$http,$location) {
    
    $scope.orders = function(){
        $http({method: 'GET', url: '/orders'})
            .success(function(data) {
                if (data.result.status == 200) {
                    $scope.users = data.result.data;
                    $scope.type = 'all';
                }
                else{
                    $location.path("/error");
                }
            })
            .error(function(data) {
                $location.path("/error");
            });
    };
    $scope.orders();
    $scope.navigate = function (){
        $location.url('/orderbyId');
    };

    $scope.valid = function (){
        $http({method: 'GET', url: '/orders?valid=1'})
            .success(function(data) {
                if (data.result.status == 200) {
                    $scope.users = data.result.data;
                    $scope.type = 'valid';
                }
                else{
                    $location.path("/error");
                }
            })
            .error(function(data) {
                $location.path("/error");
            }); 
    };

    $scope.invalid = function (){
        $http({method: 'GET', url: '/orders?valid=0'})
            .success(function(data) {
                if (data.result.status == 200) {
                    $scope.users = data.result.data;
                    $scope.type = 'valid';
                }
                else{
                    $location.path("/error");
                }
            })
            .error(function(data) {
                $location.path("/error");
            }); 
    };
    $scope.detail = function(id){
        $location.path("/orderdetails/"+id);
    };

 }]);


App.controller('orderbyIdController', ['$scope','$http','$location',
  function($scope,$http,$location) {

    $scope.getorder = function(){
        $http({method: 'GET', url: '/orders/'+$scope.orderid})

            .success(function(data) {
                if (data.result.status == 200) {
                    $scope.user = data.result.data
                    $scope.errormessage = null;
                    if (data.result.data == null){
                        $scope.errormessage = "No Orders were found..";
                    }   


                }
                else{
                    $location.path("/error");
                }
            })
            .error(function(data) {
                $location.path("/error");
            });
    };
      
 }]);

App.controller('orderdetailController', ['$scope','$http','$location','$routeParams',
  function($scope,$http,$location,$routeParams) {

    $scope.id = $routeParams.id

    $http({method: 'GET', url: '/orders/'+$scope.id})

        .success(function(data) {
            if (data.result.status == 200) {
                $scope.user = data.result.data
                $scope.errormessage = null;
                if (data.result.data == null){
                    $scope.errormessage = "No Orders were found..";
                }   


            }
            else{
                $location.path("/error");
            }
        })
        .error(function(data) {
            $location.path("/error");
        });
      
 }]);



