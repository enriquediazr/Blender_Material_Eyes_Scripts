import bpy
import numpy as np
from bpy.types import Panel, Operator
 

class ADDONNAME_PT_main_panel(Panel):
    bl_label = "Seleccionar Nodos"
    bl_idname = "ADDONNAME_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Seleccionar Nodos"
 
    def draw(self, context):
        layout = self.layout
        # addonname.myop_operator hace referencia a la parte del botón Iris
        layout.operator("addonname.myop_operator")
        # addonname.myop_operator2 hace referencia a la parte del botón Superficie Ojo
        layout.operator("addonname.myop_operator2")
 

class ADDONNAME_OT_my_op(Operator):
    # Iris para que se refleje el texto en el botón del panel
    bl_label = "Iris"
    bl_idname = "addonname.myop_operator"
    
    def execute(self, context):    
        # Array con los índices de los vértices obtenidos con el programa imprimir_nodos_seleccionados.py 
        vertices_Iris = [15,30,45,60,75,90,105,120,136,151,167,182,197,212,227,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290]        
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        # Deseleccionamos los vértices que previamente hayan podido ser seleccionados por el usuario en la aplicación
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        # Seleccionamos los vértices definidos en el Array
        for i in range(len(vertices_Iris)):
             obj.data.vertices[vertices_Iris[i]].select = True
        
        bpy.ops.object.mode_set(mode = 'EDIT')
        
        return {'FINISHED'}
    
class ADDONNAME_OT_my_op2(Operator):
    # Superficie Ojo para que se refleje el texto en el botón del panel
    bl_label = "Superficie Ojo"
    bl_idname = "addonname.myop_operator2"
    
    def execute(self, context):    
        # Array con los índices de los vértices obtenidos con el programa imprimir_nodos_seleccionados.py tras seleccionar solamente la supert¡ficie de la mesh
        vertices_Superficie = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241]      
        bpy.ops.object.mode_set(mode = 'OBJECT')
        obj = bpy.context.active_object
        bpy.ops.object.mode_set(mode = 'EDIT') 
        bpy.ops.mesh.select_mode(type="VERT")
        # Deseleccionamos los vértices que previamente hayan podido ser seleccionados por el usuario en la aplicación
        bpy.ops.mesh.select_all(action = 'DESELECT')
        bpy.ops.object.mode_set(mode = 'OBJECT')
        # Seleccionamos los vértices definidos en el Array
        for i in range(len(vertices_Superficie)):
             obj.data.vertices[vertices_Superficie[i]].select = True
        
        bpy.ops.object.mode_set(mode = 'EDIT')     
        return {'FINISHED'}

classes = [ADDONNAME_PT_main_panel, ADDONNAME_OT_my_op,ADDONNAME_OT_my_op2]
 
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()



