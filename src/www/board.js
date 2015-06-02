var app = angular.module("LNBApp",[]);
app.controller("LNBControler", function($scope, $http, $interval) {
	$interval(load_posts, 1000);
	load_posts();

	function set_time() {
		var t = new Date();
		$scope.time = t.getHours() + ":" + t.getMinutes() + ":" + t.getSeconds();
	}

	function load_posts(){
	    $http.get('http://localhost:5000/api/v1.0/posts').
	        success(function(data, status, headers, config) {
	        	if (data.posts.length === 0) {
	        		$scope.posts = [{
	        			message: 'Nothing here! ',
	        			author: 'author'
	        		}]
	        	} else {
		        	$scope.posts = data.posts;
		        }
				$scope.status = status;
				set_time();
       });
	};
});
