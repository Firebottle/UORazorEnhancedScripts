masteryBook = 0x4036B38B
waitTimeInMS = 15000

while True:

    if Misc.ReadSharedValue("BardCombat_On"):
        if Items.GetPropValueString(masteryBook,'Peacemaking Mastery'):
            if not Player.BuffsExist('Resilience'):
                Player.HeadMessage( 33, 'Resilience: Disabled' )
            if not Player.BuffsExist('Perseverance'):
                Player.HeadMessage( 33, 'Perseverance: Disabled' )

        if Items.GetPropValueString(masteryBook,'Provocation Mastery'):
            if not Player.BuffsExist('Inspire'):
                Player.HeadMessage( 33, 'Inspire: Disabled' )
            if not Player.BuffsExist('Invigorate'):
                Player.HeadMessage( 33, 'Invigorate: Disabled' )
                
        Misc.Pause(waitTimeInMS)
            
