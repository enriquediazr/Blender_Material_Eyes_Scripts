import bpy
import numpy as np
from bpy.types import Panel, Operator
 

class ADDONNAME_PT_main_panel(Panel):
    bl_label = "Imprimir Vértices Seleccionados"
    bl_idname = "ADDONNAME_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Vértices"
 
    def draw(self, context):
        layout = self.layout
        layout.operator("addonname.imprimir_vertices")
 
class ADDONNAME_OT_my_op(Operator):
    bl_label = "Imprimir"
    bl_idname = "addonname.imprimir_vertices"
    def execute(self, context):    
        
        mode = bpy.context.active_object.mode
        # Mantener el control en el modo anterior
        bpy.ops.object.mode_set(mode='OBJECT')
        # Pasar al modo objeto para actualizar los vértices seleccionados

        obj = bpy.context.object
        # Obtener el objeto actualmente seleccionado
        sel = np.zeros(len(obj.data.vertices), dtype=bool)

        obj.data.vertices.foreach_get('select', sel)
        # Crear una matriz numpy con valores vacíos para cada vértice
        print ('Los índices de los vértices son:')
        for ind in np.where(sel==True)[0]:
            # Recorrer en bucle cada uno de los vértices seleccionados actualmente
            v = obj.data.vertices[ind]
            print('{}'.format(v.index))
    
        bpy.ops.object.mode_set(mode=mode)
        # Mantener el control en el modo anterior
        
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


