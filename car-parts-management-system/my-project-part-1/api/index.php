<?php
require 'Slim/Slim.php';
require 'crud_api.php';
require 'database.php';


use Slim\Slim;
\Slim\Slim::registerAutoloader();


$app = new Slim();


$app->get('/carparts', 'getCarParts');
$app->get('/carparts/:id',  'getCarPart');
$app->post('/carparts', 'addCarPart');
$app->delete('/carparts/:id',	'deleteCarPart');
$app->put('/carparts/:id', 'updateCarPart');





$app->run();
?>



