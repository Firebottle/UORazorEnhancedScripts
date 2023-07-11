targetRange = 8
instruments = [0x0E9C, 0x0EB2, 0x0E9D, 0x0EB3]
targetDelay = 500
useTimer = True
provoDelay = 10500

Misc.ClearIgnore()

def findMobile():
    mobileFilter = Mobiles.Filter()
    mobileFilter.RangeMax = targetRange
    mobileFilter.Notorieties.Add(3)  #     3: gray, neutral
    mobileFilter.Notorieties.Add(4)  #     4: gray, criminal
    mobileFilter.Notorieties.Add(5)  #     5: orange, enemy
    mobileFilter.Notorieties.Add(6)  #     6: red, hostile
    mobileFilter.CheckIgnoreObject = True
    mobileFilter.CheckLineOfSight = True
    mobiles = Mobiles.ApplyFilter(mobileFilter)
    return mobiles

def provokeTimer():
    if Timer.Check('provoTimer') == False:
        Timer.Create('provoTimer', provoDelay)
        while Timer.Check('provoTimer'):
            Misc.Pause(500)
        print("provo ready")
    else:
        while Timer.Check('provoTimer'):
            Misc.Pause(500)
        print("provo ready")


def provokeTargets(mob1, mob2):
    Target.SetLast(mob1)
    Target.Last()
    Target.WaitForTarget(targetDelay, True)
    Target.SetLast(mob2)
    Target.Last()
    if useTimer == True:
        provokeTimer()
def provokeMobiles():
    mobs = findMobile()
    if len(mobs) >= 2:

        mob1 = Mobiles.Select(mobs,'Nearest')
        Misc.IgnoreObject(mob1)

        mobs = findMobile()
        mob2 = Mobiles.Select(mobs,'Nearest')
        Misc.IgnoreObject(mob1)

        Mobiles.Message(mob1,23,"[--X--]")
        Mobiles.Message(mob2,23,"[--X--]")

        instrument = Items.FindAllByID(instruments,-1,Player.Backpack.Serial,-1)
        if len(instrument) > 0:
            Journal.Clear()
            Player.UseSkill('Provocation')
            Target.WaitForTarget(targetDelay)

            if Journal.Search('You must wait'):
                print("wait")

            if Journal.Search('What instrument shall'):
                Target.TargetExecute(instrument[0])
                Misc.Pause(targetDelay)

            if Journal.Search('Whom do you wish to incite'):
                provokeTargets(mob1, mob2)

        else:
            print("no instruments")


while True:

    if Misc.ReadSharedValue("BardCombat_On"):
        provokeMobiles()