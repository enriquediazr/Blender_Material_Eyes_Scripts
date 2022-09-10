import bpy
import numpy as np
from bpy.types import Panel, Operator

class ADDONNAME_PT_main_panel(Panel):
    bl_label = "Cambiar Color Ojos"
    bl_idname = "ADDONNAME_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Cambiar Color Ojos"
 
    def draw(self, context):
        layout = self.layout
        # addonname.myop_operator hace referencia a la parte del botón Iris
        layout.operator("addonname.myop_operator")

class ADDONNAME_OT_my_op(Operator):
    # Iris para que se refleje el texto en el botón del panel
    bl_label = "Pulse aquí"
    bl_idname = "addonname.myop_operator"
    f = open("Indice_Material_Ojos.txt", "w")
    integer = 0
    f.write(str(integer))
    f.close()
    
    def execute(self, context):
        f = open("Indice_Material_Ojos.txt", "r")
        cont = int(f.read())
        f.close()
        
        # Seleccionar ojo izquierdo para aplicar materiales
        objectToSelect = bpy.data.objects["Ojo_Izq"]
        objectToSelect.select_set(True)    
        bpy.context.view_layer.objects.active = objectToSelect
        ojo = bpy.context.collection.objects['Ojo_Izq']
        superficie = bpy.data.materials['Superficie Ojo']
        iris = bpy.data.materials[cont]
        
        #sumar índice para cambiar color 
        f = open("Indice_Material_Ojos.txt", "w")
        if (cont == 4):
            cont = 0
        else:
            cont += 1 
        f.write(str(cont))        
        
        # Limpair materiales de mesh ojo
        ojo.data.materials.clear()
        ojo.data.materials.append(superficie)
        ojo.data.materials.append(iris)
        # Definimos los vértices que comprenden el iris en vertices_Iris
        bpy.context.object.active_material_index = 1
        vertices_Iris = [15,30,45,60,75,90,105,120,136,151,167,182,197,212,227,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290]        

        # Bucle para seleccionar los vértices definidos en la lista vertices_Iris
        for i in range(len(vertices_Iris)):
             ojo.data.vertices[vertices_Iris[i]].select = True

        bpy.ops.object.mode_set(mode = 'EDIT')

        # Asignamos el material Iris a los vértices seleccionados
        bpy.ops.object.material_slot_assign()
        bpy.ops.object.mode_set(mode = 'OBJECT')

        # Limpair materiales de mesh ojo
        objectToSelect = bpy.data.objects["Ojo_Dch"]
        objectToSelect.select_set(True)    
        bpy.context.view_layer.objects.active = objectToSelect
        ojo = bpy.context.collection.objects['Ojo_Dch']
        ojo.data.materials.clear()
        ojo.data.materials.append(superficie)
        ojo.data.materials.append(iris)
        # Definimos los vértices que comprenden el iris en vertices_Iris
        bpy.context.object.active_material_index = 1

        # Bucle para seleccionar los vértices definidos en la lista vertices_Iris
        for i in range(len(vertices_Iris)):
             ojo.data.vertices[vertices_Iris[i]].select = True

        bpy.ops.object.mode_set(mode = 'EDIT')

        # Asignamos el material Iris a los vértices seleccionados
        bpy.ops.object.material_slot_assign()
        bpy.ops.object.mode_set(mode = 'OBJECT')
        
        return {'FINISHED'}
    

classes = [ADDONNAME_PT_main_panel, ADDONNAME_OT_my_op]
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()