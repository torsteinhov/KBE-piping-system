# NX 1911
# Journal created by Hilde on Mon Mar  8 13:11:50 2021 W. Europe Standard Time
#
import math
import NXOpen
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Edit->Object Display...
    # ----------------------------------------------
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Start")
    
    theSession.SetUndoMarkName(markId1, "Class Selection Dialog")
    
    markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Class Selection")
    
    theSession.DeleteUndoMark(markId2, None)
    
    markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Class Selection")
    
    theSession.DeleteUndoMark(markId3, None)
    
    theSession.SetUndoMarkName(markId1, "Class Selection")
    
    theSession.DeleteUndoMark(markId1, None)
    
    # ----------------------------------------------
    #   Dialog Begin Edit Object Display
    # ----------------------------------------------
    markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Display")
    
    nErrs1 = theSession.UpdateManager.DoUpdate(markId4)
    
    displayModification1 = theSession.DisplayManager.NewDisplayModification()
    
    displayModification1.ApplyToAllFaces = True
    
    displayModification1.ApplyToOwningParts = False
    
    displayModification1.NewTranslucency = 95
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    body1 = workPart.Bodies.FindObject("EXTRUDE(4)")
    objects1[0] = body1
    displayModification1.Apply(objects1)
    
    displayModification1.Dispose()
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()