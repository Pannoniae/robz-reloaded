	(include "/properties/cannon.ext")
	(include "/properties/shadow/tank.inc"  scale(0.6))
	{props "vehicle" "cannon" "medium" "wheeled" "round_sandbag2" "vision_cannon_low" "muzzle_minimum"}
	{collider "cannon_small"}
	("armor_light")
	{targetSelector "cannon_at"}

	
	("wheel" args "wheelright")
	("wheel" args "wheelleft")

	("crew_wheeled_gun")
	{boarder
		{anm "gunner"
			{forward	{end "pose_pak40_gunlayer" 10}}
		}
		{anm "commander"
			{forward	{end "pose_pak40_charger" 10}}
		}
		{anm "driver1"
			{forward {end "cannon_pak40_pusher_left" 10}}
		}
		{anm "driver2"
			{forward {end "cannon_pak40_pusher_right" 10}}
		}
		{anm "seat1"
			{forward {end "pose_seat_cannon_left" 10}}
		}
		{anm "seat2"
			{forward {end "pose_seat_cannon_right" 10}}
		}
	}


	{mass 450}
	{Extension "Pak36.mdl"}
	(include "/properties/selection/cannon.inc"  scale(0.7))
	{bone "basis"
	      {limits}
	}
	{extender "cannon"
		{animation
			{switch "close"}
			{move "cannon_pak40_pusher_left" "cannon_pak40_pusher_right"}
			{aim "cannon_pak40_gunlayer" ""}
			{fire  "Cannon_gunlayer_fire-alert" "cannon_zis3_charger_fire"}
			{reload  "" "cannon_pak40_charger"}
		}
		{move {obstacle "close"}}
		{attack {obstacle "open"}}
		{rotate_ik_Limit 0}
	}

	{Chassis "track"
		("car_trace" fx("tracewheel05") step(0.07) wheell("wlf") wheelr("wrf") bonel("FXtraceL1") boner("FXtraceR1"))
		("loco_small")
	}
	{bone "turret"
		{limits -30 30}
	}
	{bone "gun_rot"
		{speed 0.01}
	}
	



