USE WebDev3_2025;

-- Table structure for table `car_parts`

DROP TABLE IF EXISTS `car_parts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;



CREATE TABLE `car_parts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `manufacturer` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `supplier` varchar(100) DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `compatible_with` varchar(100) DEFAULT NULL,
  `image` varchar(256) DEFAULT NULL,
  `age_in_years` int(11) DEFAULT NULL,
  `price` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;


/*!40101 SET character_set_client = @saved_cs_client */;


-- Dumping data for table `car_parts`

INSERT INTO `car_parts` VALUES
(1,'Brake Pad Set','Bosch','BP402','AutoZone','Brakes','Toyota Corolla','brakepad_bosch.png',1,'$45'),
(2,'Oil Filter','Mann-Filter','HU 716/2 x','NAPA Auto Parts','Engine','Audi A4','oilfilter_mann.png',2,'$18'),
(3,'Spark Plug','NGK','BKR6EIX','RockAuto','Ignition','Honda Civic','sparkplug_ngk.png',1,'$12'),
(4,'Air Filter','K&N','33-2304','Advance Auto','Air Intake','Ford Focus','airfilter_kn.png',3,'$40'),
(5,'Timing Belt Kit','Gates','TCKWP296','Carquest','Engine','Subaru Impreza','timingbelt_gates.png',2,'$120'),
(6,'Radiator Hose','Dayco','E72398','AutoZone','Cooling','Chevy Malibu','hose_dayco.png',1,'$25'),
(7,'Fuel Pump','Delphi','FG1058','O''Reilly Auto','Fuel System','Dodge Ram 1500','fuelpump_delphi.png',2,'$95'),
(8,'Clutch Kit','LUK','622117800','RockAuto','Transmission','VW Jetta','clutchkit_luk.png',3,'$160'),
(9,'Wiper Blades','Rain-X','5079279-2','Amazon','Exterior','Universal Fit','wipers_rainx.png',1,'$22'),
(10,'Headlight Bulb','Philips','H11 CrystalVision','Walmart','Lighting','Hyundai Elantra','bulb_philips.png',2,'$28'),
(11,'Battery','Optima','34/78 RedTop','Costco','Electrical','Multiple Models','battery_optima.png',2,'$180'),
(12,'Cabin Air Filter','FRAM','CF10134','Pep Boys','Air System','Toyota Camry','cabinfilter_fram.png',1,'$15');

SELECT * FROM car_parts;
