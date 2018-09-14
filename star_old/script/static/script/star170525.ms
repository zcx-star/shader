/*
Author:Zheng Chenxing
Date:2017/05/25
Email:zcx_star@163.com
*/

rollout starRollout "star" width:262 height:122
(
	button 'btn_poly' "poly" pos:[4,6] width:36 height:24 toolTip:"batch initialize poly" align:#left
	button 'btn_pivotToX' "x" pos:[44,6] width:24 height:24 toolTip:"batch set pivot to x axis" align:#left	
	button 'btn_pivotToCenter' "center" pos:[70,6] width:44 height:24 toolTip:"batch center pivot" align:#left	
	button 'btn_pivotToBottom' "bottom" pos:[116,6] width:44 height:24 toolTip:"batch set pivot to bottom center" align:#left	
	button 'btn_pivotToZero' "zero" pos:[162,6] width:36 height:24 toolTip:"batch set pivot to (0,0,0)" align:#left		
	button 'btn_deleteTurboSmooth' "deleteTB" pos:[202,6] width:56 height:24 toolTip:"batch delete all TurboSmooth" align:#left	
	button 'btn_right' "right" pos:[4,36] width:36 height:24 toolTip:"right view" align:#left
	button 'btn_back' "back" pos:[4,62] width:36 height:24 toolTip:"back view" align:#left	
	button 'btn_detachBySmoothGroup' "detach by smoothGroup" pos:[44,36] width:126 height:24 toolTip:"detach by smoothGroup" align:#left
	button 'btn_detachElementToPoly' "detach element to poly" pos:[44,62] width:126 height:24 toolTip:"detach element to poly" align:#left
	button 'btn_makeInstance' "makeInstance" pos:[174,36] width:84 height:24 toolTip:"make instance, the first is the template" align:#left		
	button 'btn_chooseInstance' "chooseInstance" pos:[174,62] width:84 height:24 toolTip:"batch choose instance" align:#left
	button 'btn_importOBJfromMAYA' "MAYA" pos:[4,92] width:36 height:24 toolTip:"settle smoothGroup if imported from MAYA" align:#left	
	button 'btn_XForm' "XFrom" pos:[44,92] width:48 height:24 toolTip:"batch XForm" align:#left
	button 'btn_importObj' "importObj" pos:[96,92] width:60 height:24 toolTip:"batch import obj" align:#left	
	button 'btn_checkFaceOver4' "Faces>4" pos:[160,92] width:54 height:24 toolTip:"select all faces>4" align:#left
	
	on btn_poly pressed do
	( 
		undo"btn_poly"on
		(
			if selection.count!=0 do
			(
				for n_poly in selection do
				(
					convertTo n_poly Editable_Poly
					n_poly.wirecolor=color 0 0 0						
					centerPivot n_poly
					if meditMaterials[1].name!="01 - Default" then
					(
						meditMaterials[1]=standard()
						meditMaterials[1].name="01 - Default"
						n_poly.material=meditMaterials[1]						
					)
					else n_poly.material=meditMaterials[1]
				)
			)	
		)		
	)
	on btn_pivotToX pressed do
	(
		undo"btn_pivotX"on
		(		
			if selection.count!=0 do for n_x in selection do n_x.pivot.x=0		 
		)
	)	
	on btn_pivotToCenter pressed do
	(
		undo "btn_pivotToCenter"on
		(
			if selection.count !=0 do for n_center in selection do centerPivot n_center						
		)
	)
	on btn_pivotToBottom pressed do
	(
		undo"btn_pivotToBottom"on
		(			
			if selection.count!=0  do
			(
				for n_bottom in selection do
				(
					centerPivot n_bottom	
					n_bottom.pivot.z=n_bottom.min.z
				)	
			)				
		)		
	)
	on btn_pivotToZero pressed do
	(
		undo"btn_pivotToZero"on
		(
			if selection.count !=0 do for n_zero in selection do n_zero.pivot=[0,0,0]
		)
	)
	on btn_deleteTurboSmooth pressed do
	(
		undo"btn_deleteTurboSmooth"on
		(
			if selection.count!=0 do
			(
				for n_delete in selection do
				(
					for n_modifiers in n_delete.modifiers.count to 1 by (-1) do
					(
						if n_delete.modifiers[n_modifiers].name=="TurboSmooth" do deleteModifier n_delete n_modifiers	
					)	
				)	
			)				
		)			
	)
	on btn_right pressed do
	(
		max vpt right			
	)
	on btn_back pressed do
	(
		max vpt back			
	)
	on btn_detachBySmoothGroup pressed do
	(
		undo"btn_detachBySmoothGroup"on
		(
			if selection.count!=1 then messagebox "please select only one object"
			else  	
			(	
				totalFace=$.faces.count
				while (totalFace!=0) do 
				(
					smoothGroup=polyOp.getFaceSmoothGroup $ 1
					if smoothGroup==0 then
					(
						polyOp.detachFaces $ #{1} asNode:true
						totalFace=totalFace-1
					)
					else
					(
						$.EditablePoly.selectBySmoothGroup smoothGroup	
						faceSet=polyOp.getFaceSelection $
						tempfaceSet=faceSet as array
						polyOp.detachFaces $ faceSet asNode:true 
						totalFace=totalFace-tempfaceSet.count
					)	
				)	
				delete $
			)				
		)	
	)
	on btn_detachElementToPoly pressed do
	(
		undo"btn_detachElementToPoly pressed"on
		(
			if selection.count!=1 then messagebox "please select only one object"
			else 
			(
				while ($.faces.count!=0) do
				(				
					faceID = polyop.getElementsUsingFace $ #{1}
					polyOp.detachFaces $ faceID asNode:true			
				)			
				delete $					
			)
		)
	)
	on btn_makeInstance pressed do
	(
		undo"btn_makeInstance"on
		(
			if selection.count!=0 do
			(
				if selection.count==1 then messagebox"please select all objects"
				else for n_instance=2 to selection.count do instanceReplace selection[n_instance] selection[1]	
			)			
		)
	)
	on btn_chooseInstance pressed do
	(
		undo"btn_chooseInstance"on
		(	
			instanceSet=#()
			for n_instance in selection do
			(
				InstanceMgr.GetInstances n_instance &instances
				join instanceSet instances				
			)
			select instanceSet	
			instanceSet=#()		
		)
	)
	on btn_importOBJfromMAYA pressed do
	(
		undo"btn_importOBJfromMAYA pressed"on
		(
			if selection.count!=1 then messagebox "please select only one object"
			else				
			(
				myObj = $
				convertToPoly myObj
				edgeCount = polyop.getNumEdges myObj
				allFace = for i in myObj.Faces collect i.index
				allFace = allFace as bitarray
	
				myMod = EditNormals()
				addModifier myObj myMod
				setCommandPanelTaskMode #modify 
				modPanel.setCurrentObject myMod
	
				--select hard edges
				hardEdges = #{}
				for i =1 to edgeCount do
				(
					edgeNormals = #{}
					myMod.ConvertEdgeSelection #{i} edgeNormals
					if edgeNormals.numberSet>2 do hardEdges[i]=true
				)
				deleteModifier myObj myMod
				modPanel.setCurrentObject myObj.baseObject
				subObjectLevel = 2
				myObj.SetSelection #Edge hardEdges
	
				myMod = Edit_Poly ()
				addModifier myObj myMod
	
				--clear smoothing group
				subobjectLevel = 4
				myMod.SetSelection #Face allFace
				myMod.SetOperation #SetSmooth
				myMod.smoothingGroupsToClear = -1
				myMod.smoothingGroupsToSet = 1
	
				subobjectLevel = 2
				myMod.ButtonOp #MakeHardEdges
	
				subobjectLevel = 0
				collapseStack myObj
				messagebox "success!"				
			)
		)
	)
	on btn_XForm pressed do
	(
		undo"btn_XForm"on
		(
			if selection.count!=0 do
			(
				for n_XForm in selection do
				(
					ResetXForm n_XForm
					convertTo n_XForm Editable_Poly
				)
			)	
		)			
	)
	on btn_importObj pressed do
	(
		filePath=getSavePath caption:"star" initialDir:maxfilepath 
		if filePath!=undefined do
		(
			objPath=filePath+"\*.obj"
			objFile = getFiles objPath		
			for n_path in objFile do   
			(  
				if (doesfileexist n_path) do importFile n_path #noPrompt using:Wavefront_Object 			  
			) 				
		)		
	)
	on btn_checkFaceOver4 pressed do
	(
		undo"btn_checkFaceOvev4"on
		(
			if selection.count!=1 then messagebox "please select only one object"
			else
			(
				checkFaceSet=#()
				arr_faceSet = for i in $.Faces collect i.index
				arr_faceSet = arr_faceSet as bitarray
				for n_face in arr_faceSet do
				(
					edgeSet=polyOp.getFaceEdges $ n_face
					if edgeSet.count>4 do append checkFaceSet n_face
				)
				if checkFaceSet.count==0 then messagebox"success"
				else 
				(
					setCommandPanelTaskMode #modify 
					subObjectLevel = 4
					polyOp.setFaceSelection $ checkFaceSet
				)
				checkFaceSet=#()	
			)
		)
	)
)
createDialog starRollout