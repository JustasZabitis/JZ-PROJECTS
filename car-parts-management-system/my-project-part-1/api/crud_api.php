<?php

// RETRIEVE ALL CAR PARTS
function getCarParts() {
	$query = "SELECT * FROM car_parts ORDER BY name";
	try {
		global $db;
		$car_parts = $db->query($query);  
		$car_parts = $car_parts->fetchAll(PDO::FETCH_ASSOC);
		header("Content-Type: application/json", true);


		// Check if any car parts were found
		if ($car_parts && count($car_parts) > 0) {
			http_response_code(200); // OK
			echo json_encode([
				"status" => 200,
				"message" => "Car parts retrieved successfully",
				"car_part" => $car_parts
			]);
		} else {
			http_response_code(404); // Not Found
			echo json_encode([
				"status" => 404,
				"message" => "No Parts are Found"
			]);
		}
	} catch(PDOException $e) {
		echo json_encode([
			"error" => $e->getMessage()
		]);
	}
}



// RETRIEVE A SINGLE CAR PART BY ID
function getCarPart($id) {
	$query = "SELECT * FROM car_parts WHERE id = '$id'";
	try {
		global $db;
		$car_parts = $db->query($query);  
		$car_parts = $car_parts->fetch(PDO::FETCH_ASSOC);
		header("Content-Type: application/json", true);


		// Check if the car part was found
		if ($car_parts) {
			http_response_code(200); // OK
			echo json_encode([
				"status" => 200,
				"message" => "Car part found",
				"car_part" => $car_parts
			]);
		} else {
			http_response_code(404); // Not Found
			echo json_encode([
				"status" => 404,
				"message" => "No Parts are Found"
			]);
		}
	} catch(PDOException $e) {
		echo json_encode([
			"error" => $e->getMessage()
		]);
	}
}



// ADD A NEW CAR PART
function addCarPart() {
	global $app;
	$request = $app->request();
	$car_parts = json_decode($request->getBody());
	$id = $car_parts->id;
	$name = $car_parts->name;
	$manufacturer = $car_parts->manufacturer;
	$model = $car_parts->model;
	$supplier = $car_parts->supplier;
	$category = $car_parts->category;
	$compatible_with = $car_parts->compatible_with;
	$image = $car_parts->image;
	$age_in_years = $car_parts->age_in_years;
	$price = $car_parts->price;
	
	$query = "INSERT INTO car_parts
				(id, name, manufacturer, model, supplier, category, compatible_with, image, age_in_years, price)
			  VALUES
				('$id', '$name', '$manufacturer', '$model', '$supplier', '$category', '$compatible_with', '$image', '$age_in_years', '$price')";
	try {
		global $db;
		$db->exec($query);
		$car_parts->id = $db->lastInsertId();


		// Respond with the created car part

		http_response_code(201); // Created
		echo json_encode([
			"status" => 201,
			"message" => "Car part added successfully",
			"car_part" => $car_parts
		]); 
	} catch(PDOException $e) {
		http_response_code(400); // Bad Request
		echo json_encode([
			"status" => 400,
			"error" => $e->getMessage()
		]);
	}
}



// UPDATE AN EXISTING CAR PART
function updateCarPart($id) {
	global $app;
	$request = $app->request();
	$car_parts = json_decode($request->getBody());
	$id = $car_parts->id;
	$name = $car_parts->name;
	$manufacturer = $car_parts->manufacturer;
	$model = $car_parts->model;
	$supplier = $car_parts->supplier;
	$category = $car_parts->category;
	$compatible_with = $car_parts->compatible_with;
	$image = $car_parts->image;
	$age_in_years = $car_parts->age_in_years;
	$price = $car_parts->price;

	$query = "UPDATE car_parts 
			  SET name='$name', manufacturer='$manufacturer', model='$model', supplier='$supplier', category='$category', 
				  compatible_with='$compatible_with', image='$image', age_in_years='$age_in_years', price='$price' 
			  WHERE id='$id'";
	try {
		global $db;
		$result = $db->exec($query); 


		// Check if the update was successful
		if ($result > 0) {
			http_response_code(200); // OK
			echo json_encode([
				"status" => 200,
				"message" => "Car part updated successfully",
				"car_part" => $car_parts
			]);
		} else {
			http_response_code(404); // Not Found
			echo json_encode([
				"status" => 404,
				"message" => "No Parts are Found"
			]);
		}
	} catch(PDOException $e) {
		http_response_code(400); // Bad Request
		echo json_encode([
			"status" => 400,
			"error" => $e->getMessage()
		]);
	}
}



// DELETE A CAR PART BY ID
function deleteCarPart($id) {
	$query = "DELETE FROM car_parts WHERE id = '$id'";
	try {
		global $db;
		$result = $db->exec($query); 


		// Check if the deletion was successful
		if ($result > 0) {
			http_response_code(200); // OK 
			echo json_encode([
				"status" => 200,
				"message" => "Car part deleted successfully"
			]);
		} else {
			http_response_code(404); // Not Found
			echo json_encode([
				"status" => 404,
				"message" => "No Parts are Found"
			]);
		}
	} catch(PDOException $e) {
		http_response_code(500); // Internal Server Error
		echo json_encode([
			"status" => 500,
			"error" => $e->getMessage()
		]);
	}
}
