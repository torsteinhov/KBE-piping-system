# NX 1911
# Journal created by Hilde on Thu Mar 25 17:48:05 2021 W. Europe Standard Time
#
import math
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
def main() : 

    theSession  = NXOpen.Session.GetSession()
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    # ----------------------------------------------
    #   Menu: Tools->Journal->Play...
    # ----------------------------------------------
    part1 = theSession.Parts.Work
    
    blockFeatureBuilder1 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    blockFeatureBuilder1.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    
    originPoint1 = NXOpen.Point3d(0.0, 0.0, 0.0)
    blockFeatureBuilder1.SetOriginAndLengths(originPoint1, "3000", "3000", "3000")
    
    booleanOperation1 = blockFeatureBuilder1.BooleanOption
    
    booleanOperation1.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject1 = blockFeatureBuilder1.Commit()
    
    block1 = nXObject1
    bodies1 = block1.GetBodies()
    
    blockFeatureBuilder1.Destroy()
    
    displayModification1 = theSession.DisplayManager.NewDisplayModification()
    
    displayModification1.ApplyToAllFaces = True
    
    displayModification1.ApplyToOwningParts = False
    
    displayModification1.NewColor = 40
    
    displayModification1.NewTranslucency = 95
    
    objects1 = [NXOpen.DisplayableObject.Null] * 1 
    objects1[0] = bodies1[0]
    displayModification1.Apply(objects1)
    
    displayModification1.Dispose()
    part2 = theSession.Parts.Work
    
    cylinderBuilder1 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression1 = cylinderBuilder1.Diameter
    
    expression1.RightHandSide = "50.8"
    
    expression2 = cylinderBuilder1.Height
    
    expression2.RightHandSide = "5"
    
    origin1 = NXOpen.Point3d(0.0, 1500.0, 1500.0)
    cylinderBuilder1.Origin = origin1
    
    vector1 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    cylinderBuilder1.Direction = vector1
    
    booleanOperation2 = cylinderBuilder1.BooleanOption
    
    booleanOperation2.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject2 = cylinderBuilder1.Commit()
    
    cylinder1 = nXObject2
    bodies2 = cylinder1.GetBodies()
    
    cylinderBuilder1.Destroy()
    
    part3 = theSession.Parts.Work
    
    booleanBuilder1 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder1.Target = bodies1[0]
    
    booleanBuilder1.Tool = bodies2[0]
    
    booleanBuilder1.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject3 = booleanBuilder1.Commit()
    
    booleanBuilder1.Destroy()
    
    part4 = theSession.Parts.Work
    
    cylinderBuilder2 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression3 = cylinderBuilder2.Diameter
    
    expression3.RightHandSide = "50.8"
    
    expression4 = cylinderBuilder2.Height
    
    expression4.RightHandSide = "5"
    
    origin2 = NXOpen.Point3d(3000.0, 1500.0, 1500.0)
    cylinderBuilder2.Origin = origin2
    
    vector2 = NXOpen.Vector3d(-1.0, 0.0, 0.0)
    cylinderBuilder2.Direction = vector2
    
    booleanOperation3 = cylinderBuilder2.BooleanOption
    
    booleanOperation3.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject4 = cylinderBuilder2.Commit()
    
    cylinder2 = nXObject4
    bodies3 = cylinder2.GetBodies()
    
    cylinderBuilder2.Destroy()
    
    part5 = theSession.Parts.Work
    
    booleanBuilder2 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder2.Target = bodies1[0]
    
    booleanBuilder2.Tool = bodies3[0]
    
    booleanBuilder2.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject5 = booleanBuilder2.Commit()
    
    booleanBuilder2.Destroy()
    
    part6 = theSession.Parts.Work
    
    blockFeatureBuilder2 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    blockFeatureBuilder2.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    
    originPoint2 = NXOpen.Point3d(50.0, 50.0, 50.0)
    blockFeatureBuilder2.SetOriginAndLengths(originPoint2, "70", "70", "70")
    
    booleanOperation4 = blockFeatureBuilder2.BooleanOption
    
    booleanOperation4.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject6 = blockFeatureBuilder2.Commit()
    
    block2 = nXObject6
    bodies4 = block2.GetBodies()
    
    blockFeatureBuilder2.Destroy()
    
    part7 = theSession.Parts.Work
    
    cylinderBuilder3 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression5 = cylinderBuilder3.Diameter
    
    expression5.RightHandSide = "50.8"
    
    expression6 = cylinderBuilder3.Height
    
    expression6.RightHandSide = "5"
    
    origin3 = NXOpen.Point3d(50.0, 85.0, 85.0)
    cylinderBuilder3.Origin = origin3
    
    vector3 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    cylinderBuilder3.Direction = vector3
    
    booleanOperation5 = cylinderBuilder3.BooleanOption
    
    booleanOperation5.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject7 = cylinderBuilder3.Commit()
    
    cylinder3 = nXObject7
    bodies5 = cylinder3.GetBodies()
    
    cylinderBuilder3.Destroy()
    
    part8 = theSession.Parts.Work
    
    booleanBuilder3 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder3.Target = bodies4[0]
    
    booleanBuilder3.Tool = bodies5[0]
    
    booleanBuilder3.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject8 = booleanBuilder3.Commit()
    
    booleanBuilder3.Destroy()
    
    part9 = theSession.Parts.Work
    
    cylinderBuilder4 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression7 = cylinderBuilder4.Diameter
    
    expression7.RightHandSide = "50.8"
    
    expression8 = cylinderBuilder4.Height
    
    expression8.RightHandSide = "5"
    
    origin4 = NXOpen.Point3d(120.0, 85.0, 85.0)
    cylinderBuilder4.Origin = origin4
    
    vector4 = NXOpen.Vector3d(-1.0, 0.0, 0.0)
    cylinderBuilder4.Direction = vector4
    
    booleanOperation6 = cylinderBuilder4.BooleanOption
    
    booleanOperation6.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject9 = cylinderBuilder4.Commit()
    
    cylinder4 = nXObject9
    bodies6 = cylinder4.GetBodies()
    
    cylinderBuilder4.Destroy()
    
    part10 = theSession.Parts.Work
    
    booleanBuilder4 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder4.Target = bodies4[0]
    
    booleanBuilder4.Tool = bodies6[0]
    
    booleanBuilder4.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject10 = booleanBuilder4.Commit()
    
    booleanBuilder4.Destroy()
    
    part11 = theSession.Parts.Work
    
    blockFeatureBuilder3 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    blockFeatureBuilder3.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    
    originPoint3 = NXOpen.Point3d(150.0, 150.0, 150.0)
    blockFeatureBuilder3.SetOriginAndLengths(originPoint3, "150", "150", "150")
    
    booleanOperation7 = blockFeatureBuilder3.BooleanOption
    
    booleanOperation7.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject11 = blockFeatureBuilder3.Commit()
    
    block3 = nXObject11
    bodies7 = block3.GetBodies()
    
    blockFeatureBuilder3.Destroy()
    
    part12 = theSession.Parts.Work
    
    cylinderBuilder5 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression9 = cylinderBuilder5.Diameter
    
    expression9.RightHandSide = "50.8"
    
    expression10 = cylinderBuilder5.Height
    
    expression10.RightHandSide = "5"
    
    origin5 = NXOpen.Point3d(150.0, 225.0, 225.0)
    cylinderBuilder5.Origin = origin5
    
    vector5 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    cylinderBuilder5.Direction = vector5
    
    booleanOperation8 = cylinderBuilder5.BooleanOption
    
    booleanOperation8.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject12 = cylinderBuilder5.Commit()
    
    cylinder5 = nXObject12
    bodies8 = cylinder5.GetBodies()
    
    cylinderBuilder5.Destroy()
    
    part13 = theSession.Parts.Work
    
    booleanBuilder5 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder5.Target = bodies7[0]
    
    booleanBuilder5.Tool = bodies8[0]
    
    booleanBuilder5.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject13 = booleanBuilder5.Commit()
    
    booleanBuilder5.Destroy()
    
    part14 = theSession.Parts.Work
    
    cylinderBuilder6 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression11 = cylinderBuilder6.Diameter
    
    expression11.RightHandSide = "50.8"
    
    expression12 = cylinderBuilder6.Height
    
    expression12.RightHandSide = "5"
    
    origin6 = NXOpen.Point3d(300.0, 225.0, 225.0)
    cylinderBuilder6.Origin = origin6
    
    vector6 = NXOpen.Vector3d(-1.0, 0.0, 0.0)
    cylinderBuilder6.Direction = vector6
    
    booleanOperation9 = cylinderBuilder6.BooleanOption
    
    booleanOperation9.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject14 = cylinderBuilder6.Commit()
    
    cylinder6 = nXObject14
    bodies9 = cylinder6.GetBodies()
    
    cylinderBuilder6.Destroy()
    
    part15 = theSession.Parts.Work
    
    booleanBuilder6 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder6.Target = bodies7[0]
    
    booleanBuilder6.Tool = bodies9[0]
    
    booleanBuilder6.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject15 = booleanBuilder6.Commit()
    
    booleanBuilder6.Destroy()
    
    part16 = theSession.Parts.Work
    
    blockFeatureBuilder4 = workPart.Features.CreateBlockFeatureBuilder(NXOpen.Features.Feature.Null)
    
    blockFeatureBuilder4.Type = NXOpen.Features.BlockFeatureBuilder.Types.OriginAndEdgeLengths
    
    originPoint4 = NXOpen.Point3d(1000.0, 1000.0, 1000.0)
    blockFeatureBuilder4.SetOriginAndLengths(originPoint4, "1000", "1000", "1000")
    
    booleanOperation10 = blockFeatureBuilder4.BooleanOption
    
    booleanOperation10.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject16 = blockFeatureBuilder4.Commit()
    
    block4 = nXObject16
    bodies10 = block4.GetBodies()
    
    blockFeatureBuilder4.Destroy()
    
    part17 = theSession.Parts.Work
    
    cylinderBuilder7 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression13 = cylinderBuilder7.Diameter
    
    expression13.RightHandSide = "50.8"
    
    expression14 = cylinderBuilder7.Height
    
    expression14.RightHandSide = "5"
    
    origin7 = NXOpen.Point3d(1000.0, 1500.0, 1500.0)
    cylinderBuilder7.Origin = origin7
    
    vector7 = NXOpen.Vector3d(1.0, 0.0, 0.0)
    cylinderBuilder7.Direction = vector7
    
    booleanOperation11 = cylinderBuilder7.BooleanOption
    
    booleanOperation11.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject17 = cylinderBuilder7.Commit()
    
    cylinder7 = nXObject17
    bodies11 = cylinder7.GetBodies()
    
    cylinderBuilder7.Destroy()
    
    part18 = theSession.Parts.Work
    
    booleanBuilder7 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder7.Target = bodies10[0]
    
    booleanBuilder7.Tool = bodies11[0]
    
    booleanBuilder7.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject18 = booleanBuilder7.Commit()
    
    booleanBuilder7.Destroy()
    
    part19 = theSession.Parts.Work
    
    cylinderBuilder8 = workPart.Features.CreateCylinderBuilder(NXOpen.Features.Feature.Null)
    
    expression15 = cylinderBuilder8.Diameter
    
    expression15.RightHandSide = "50.8"
    
    expression16 = cylinderBuilder8.Height
    
    expression16.RightHandSide = "5"
    
    origin8 = NXOpen.Point3d(2000.0, 1500.0, 1500.0)
    cylinderBuilder8.Origin = origin8
    
    vector8 = NXOpen.Vector3d(-1.0, 0.0, 0.0)
    cylinderBuilder8.Direction = vector8
    
    booleanOperation12 = cylinderBuilder8.BooleanOption
    
    booleanOperation12.Type = NXOpen.GeometricUtilities.BooleanOperation.BooleanType.Create
    
    nXObject19 = cylinderBuilder8.Commit()
    
    cylinder8 = nXObject19
    bodies12 = cylinder8.GetBodies()
    
    cylinderBuilder8.Destroy()
    
    part20 = theSession.Parts.Work
    
    booleanBuilder8 = workPart.Features.CreateBooleanBuilder(NXOpen.Features.BooleanFeature.Null)
    
    booleanBuilder8.Target = bodies10[0]
    
    booleanBuilder8.Tool = bodies12[0]
    
    booleanBuilder8.Operation = NXOpen.Features.Feature.BooleanType.Subtract
    
    nXObject20 = booleanBuilder8.Commit()
    
    booleanBuilder8.Destroy()
    
    # ----------------------------------------------
    #   Menu: Orient View->Trimetric
    # ----------------------------------------------
    workPart.ModelingViews.WorkView.Orient(NXOpen.View.Canned.Trimetric, NXOpen.View.ScaleAdjustment.Fit)
    
    # ----------------------------------------------
    #   Menu: Tools->Journal->Stop Recording
    # ----------------------------------------------
    
if __name__ == '__main__':
    main()