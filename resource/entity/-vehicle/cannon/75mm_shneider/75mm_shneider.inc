
	(include "/properties/cannon.ext")
	(include "/properties/shadow/tank.inc"  scale(0.6))
	{props "vehicle" "cannon" "medium" "wheeled" "round_sandbag2" "vision_cannon_medium" "muzzle_medium"}
	{targetSelector "cannon_sup"}

	
	("armor_medium")

	("wheel" args "wheelright")
	("wheel" args "wheelleft")

	("crew_wheeled_gun")

	{boarder
		{anm "gunner"
			{forward	{end "pose_pdr25_gunlayer" 10}}
		}
		{anm "commander"
			{forward	{end "pose_pdr25_charger" 10}}
		}
		{anm "driver1"
			{forward {end "cannon_pak40_pusher_left" 10}}
		}
		{anm "driver2"
			{forward {end "cannon_pak40_pusher_right" 10}}
		}
		{anm "seat1"
			{forward {end "pose_seat_cannon1_right" 10}}
		}
		{anm "seat2"
			{forward {end "pose_seat_cannon1_right" 10}}
		}
	}

	{mass 1100}
	{Extension "75mm_shneider.mdl"}
	(include "/properties/selection/cannon.inc"  scale(0.7))
	{bone "basis"
	      {limits}
	      {speed 0.007}
	}
	{extender "cannon"
		{animation
			{move	"cannon_pak40_pusher_left" "cannon_pak40_pusher_right"}
			{aim	"Cannon_pdr25_gunlayer" ""}
			{fire	"Cannon_pdr25_gunlayer_fire-alert" "cannon_pdr25_charger_fire"}
			{reload	"" "Cannon_pdr25_charger"}
		}
		{move {obstacle "close"}}
		{attack {obstacle "open"}}
		{rotate_ik_Limit 30}
	}
	{Chassis "track"
		("car_trace" fx("tracewheel05") step(0.07) wheell("wlf") wheelr("wrf") bonel("FXtraceL1") boner("FXtraceR1"))
		("loco_medium")
	}
	{bone "gun_rot"
		{speed 0.001}
	}

