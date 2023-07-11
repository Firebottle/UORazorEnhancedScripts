if Misc.ReadSharedValue("BardCombat_On") == False:
    Misc.SetSharedValue("BardCombat_On", True)
    Player.HeadMessage( 0x0044, 'Bard Combat: Enabled' )
    Misc.Pause(1)
    
elif Misc.ReadSharedValue("BardCombat_On") == True:
    Misc.SetSharedValue("BardCombat_On", False)
    Player.HeadMessage( 33, 'Bard Combat: Disabled' )
    Misc.Pause(1)