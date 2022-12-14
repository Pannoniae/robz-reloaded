
	(include "/properties/car.ext")
	(include "/properties/shadow/tank.inc"  scale(1.0))
	(include "/properties/selection/vehicle.inc"  scale(1.1))
	{collider "truck"}
	{props "vehicle" "car" "truck" "wheeled" "vision_vehicle_medium"}
	{able "emit_on_attack"}
	("armor_medium" args 1.0)

	("crew_2_human")
	("board_animation"
		place(driver)
		board_begin(board_big-midcar_driver)
		board_end(seat_driver_car)
		base(doorleft)
	)
	("board_animation"
		place(commander)
		board_begin(board_big-midcar)
		board_end(seat_passenger)
		base(doorright)
	)

	{boarder
		{anm "passenger"
			{forward	{begin	"board_body"} {end "seat_passenger"}}
			{reverse 	{end	"emit_body" 1}}
		}
	}

	("wheel" args "wheelright1")
	("wheel" args "wheelleft1")
	("wheel" args "wheelright2")
	("wheel" args "wheelleft2")
	
	{Volume "bodyback"
		{thickness 3}
	}
	{mass 3100}



	{Chassis
		{Locomotion ("locomotion")
      		{MaxSpeed   34}
				(mod "mp"
					{maxspeed   31}
				)
	  		{maxSpeedAtMaxTurn 17}
      		{TurnRadius 6}
      	}
		{FuelBag
			{volume 60 }	
			{rate	15 }   
			{remain 60 }
			{fuel "fuel"}
		}
		("car_trace" fx("tracewheel03") step(0.08) wheell("wlf") wheelr("wrf") bonel("FXtraceL1") boner("FXtraceR1"))
		("car_trace" fx("tracewheel03") step(0.08) wheell("wlr") wheelr("wrr") bonel("FXtraceL2") boner("FXtraceR2"))
	}
	{Extension "mercedesl3000.mdl"}
	{extender "shield"
		{on}
	}
	{component "shield"	
		{RepairTime 10}
	}
	{volume "shield"
		{thickness 0.3}
	}
	{component "cabin"	
		{RepairTime 12}
	}
	{volume "cabin"
		{thickness 3}
	}
	{volume "engine"
		{thickness 3}
	}
	{Volume "Body"
		{tags "body"}
		{component "body"}
		{thickness 7}   
	}
 	

