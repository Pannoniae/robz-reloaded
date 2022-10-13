
	(include "/properties/cannon.ext")
	{props "vehicle" "cannon" "medium" "wheeled" "round_sandbag2" "vision_cannon_medium" "muzzle_medium"}
	
	{targetSelector "cannon_at"}

	("armor_medium")
	
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

	{Weaponry

		{place "gun"
			{weapon "75mm_pak40" filling "ger_bullet75_pak40 ap"}
			{RestoreIKAfterAim}
			{Rotate}
			("abm_field_gun")
		}
	}
	{mass 1500}
	{Extension "Pak40.mdl"}
	(include "/properties/selection/cannon.inc"  scale(0.7))
	
	{extender "cannon"
		{animation
			{switch "close"}
			{move "cannon_pak40_pusher_left" "cannon_pak40_pusher_right"}
			{aim "cannon_pak40_gunlayer" ""}
			{fire  "Cannon_gunlayer_fire-alert" "Cannon_zis3_charger_fire 0.2"}
			{reload  "" "cannon_pak40_charger"}
		}
		{move {obstacle "close"}}
		{attack {obstacle "open"}}
		{rotate_ik_Limit 0}
	}

	{Chassis "track"
		("car_trace" fx("tracewheel05") step(0.07) wheell("wlf") wheelr("wrf") bonel("FXtraceL1") boner("FXtraceR1"))
		("loco_medium")
	}
	{bone "turret"
		{limits -30 30}
		{speed 0.006}
	}
	{bone "gun_rot"
		{speed 0.005}
	}
	{bone "basis"
	    {limits}
	    {speed 0.007}
	}

