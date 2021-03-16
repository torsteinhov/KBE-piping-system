# Basic class in Python
# NXPython/shapes/Block.py
import math
import NXOpen
import NXOpen.Annotations
import NXOpen.Features
import NXOpen.GeometricUtilities
import NXOpen.Preferences


class Block:

    #    length = 0         # class variable shared by all instances
    #	width = ...

    def getVolume(self):
        return self.length * self.width * self.height

    def __init__(self, x, y, z, length, width, height, color, material):
        self.length = length  # instance variable unique to each instance
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.material = material

    def initForNX(self, x, y, z, length, width, height, color, material):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        #   The block
        blockfeaturebuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Block.Null)
        blockfeaturebuilder1.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths

        origBlock = NXOpen.Point3d(float(x), float(y), float(z))
        blockfeaturebuilder1.SetOriginAndLengths(origBlock, str(length), str(width), str(height))
        blockfeaturebuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

        self.body = blockfeaturebuilder1.Commit().GetBodies()[0]
        origBlock.SetName("The Block")
        blockfeaturebuilder1.Destroy()

    def initForNX(self):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work
        
        

        #   The block
        blockfeaturebuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Block.Null)
        blockfeaturebuilder1.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths

        origBlock = NXOpen.Point3d(float(self.x), float(self.y), float(self.z))
        blockfeaturebuilder1.SetOriginAndLengths(origBlock, str(self.length), str(self.width), str(self.height))
        blockfeaturebuilder1.BooleanOption.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create

        """
        # this eddits all of the blocks in the view!
        if self.material.find("SeeThrough") != -1:
            displayPart = theSession.Parts.Display #for see through the block
            workPart.ModelingViews.WorkView.RenderingStyle = NXOpen.View.RenderingStyleType.WireframeWithDimEdges # applying the see through
        """
        """
        if self.material.find("SeeThrough") != -1:
            displayPart = theSession.Parts.Display
            #markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Edit Object Display")
            #nErrs1 = theSession.UpdateManager.DoUpdate(markId4)
            
            displayModification1 = theSession.DisplayManager.NewDisplayModification()
    
            displayModification1.ApplyToAllFaces = True
            
            displayModification1.ApplyToOwningParts = False
            
            displayModification1.NewColor = 40
            
            displayModification1.NewTranslucency = 96
            
            objects1 = [NXOpen.DisplayableObject.Null] * 1 
            body1 = workPart.Bodies.FindObject("EXTRUDE(4)")
            objects1[0] = body1
            displayModification1.Apply(objects1)
            
            displayModification1.Dispose()
            
            displayModification1 = theSession.DisplayManager.NewDisplayModification()
            
            displayModification1.ApplyToAllFaces = True
            
            displayModification1.ApplyToOwningParts = False
            
            displayModification1.NewTranslucency = 95
            
            #objects1 = [NXOpen.DisplayableObject.Null] * 1 
            #self.workPart.Bodies.FindObject()
            #objects1[0] = body1
            #self.displayModification1.Apply()
            
            displayModification1.Dispose()
        """
        self.body = blockfeaturebuilder1.Commit().GetBodies()[0]
        blockfeaturebuilder1.Destroy()

    def subtract(self, tool):
        theSession = NXOpen.Session.GetSession()
        workPart = theSession.Parts.Work

        subtractfeaturebuilder1 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)

        subtractfeaturebuilder1.Target = self.body  # bodyTarget_.GetBodies()[0] # From where to subtract
        subtractfeaturebuilder1.Tool = tool.body  # What to subtract
        subtractfeaturebuilder1.Operation = NXOpen.Features.FeatureBooleanType.Subtract

        subtractfeaturebuilder1.Commit()
        subtractfeaturebuilder1.Destroy()
    """
    def makeSeeThrough(self, t):
        theSession  = NXOpen.Session.GetSession()
        
        displayModification1 = theSession.DisplayManager.NewDisplayModification()
        displayModification1.ApplyToAllFaces = True
        displayModification1.ApplyToOwningParts = False
        displayModification1.NewColor = 40
        displayModification1.NewTranslucency = t
        objects1 = [NXOpen.DisplayableObject.Null] * 1 
        body1 = self.body
        objects1[0] = body1
        displayModification1.Apply(objects1)
        displayModification1.Dispose()
    """