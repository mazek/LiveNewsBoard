var mockDataForThisTest = "json=" + encodeURI(JSON.stringify([
	{
	    id: 1,
	    firstName: "Peter",
	    lastName: "Jhons"
	},
	{
		id: 2,
		firstName: "David",
		lastName: "Bowie"
	}
]));


var app = angular.module('myApp', []);

function PeopleCtrl($scope, $http) {

    $scope.people = [];

    $scope.loadPeople = function() {
        var httpRequest = $http({
            method: 'POST',
            url: '/echo/json/',
            data: mockDataForThisTest

        }).success(function(data, status) {
            $scope.people = data;
        });

    };

}

