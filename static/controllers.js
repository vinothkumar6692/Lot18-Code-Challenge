App.controller('uploadController', ['$scope','$http','$location',
  function($scope,$http,$location) {

 

    $scope.uploadFile = function() {
        var f = document.getElementById('file').files[0]; 
        var formData = new FormData();
        formData.append('file', f);

        $http({method: 'POST', url: '/import/', data: formData, headers: {'Content-Type': undefined}, transformRequest: angular.identity})
            .success(function(data) {
                console.log(data);
                if (data.result.status == 200){
                    console.log("done");
                    $location.path("/orders");
                }
                else{
                    console.log("error");
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

    console.log("orders");
    $http({method: 'GET', url: '/orders'})
        .success(function(data) {
            if (data.result.status == 200) {
                $scope.users = data.result.data
            }
            else{
                $location.path("/error");
            }
        })
        .error(function(data) {
            $location.path("/error");
        });

    $scope.navigate = function (){
        $location.url('/orderbyId');
    };

    $scope.valid = function (){
        $http({method: 'GET', url: '/orders?valid=1'})
            .success(function(data) {
                if (data.result.status == 200) {
                    $scope.users = data.result.data
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
                    $scope.users = data.result.data
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


