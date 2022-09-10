import bpy

####################################################################### SUPERFICIE OJO #######################################################################
obj = bpy.context.object  # Asignación de la mesh seleccionada con el puntero
mat = bpy.data.materials.new(name='Superficie Ojo')  # Creación del material
# Configuración del material
obj.data.materials.append(mat)  # Asignación del material
obj = bpy.context.active_object

new_mat = bpy.data.materials.get('Superficie Ojo')
if not new_mat:
    new_mat = bpy.data.materials.new('Superficie Ojo')
    
# Activamos las refracción para poder ver la pupila
bpy.context.object.active_material.use_screen_refraction = True

# habilitaremos el uso de nodos, ya que sin ello no podríamos crear ninguno
new_mat.use_nodes = True

# Definimos la estructura que tendran los nodos y los enlaces para su creación
node_tree = new_mat.node_tree
nodos = node_tree.nodes
nodos.clear()
    
enlaces = node_tree.links
enlaces.clear()
    
######### Nodos #########

# Frame_S será el nodo que englobe el nodo Mapping, el nodo Voronoi Texture que da textura voronoi a los vasos sanguíneos de menor longitud y el nodo ColorRamp
nodo_actual = nodos.new(type='NodeFrame')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.label = 'S'
nodo_actual.label_size = 20
nodo_actual.location = (-1756.5, 1353.1)
nodo_actual.name = 'Frame_S'
nodo_actual.select = False
nodo_actual.width = 800

# Frame_M será el nodo que englobe el nodo Mapping, el nodo Voronoi Texture que da textura voronoi a los vasos sanguíneos de longitud medio y el nodo ColorRamp
nodo_actual = nodos.new(type='NodeFrame')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.label = 'M'
nodo_actual.label_size = 20
nodo_actual.location = (-1787.8, 961)
nodo_actual.name = 'Frame_M'
nodo_actual.select = False
nodo_actual.width = 800

# Frame_L será el nodo que englobe el nodo Mapping, el nodo Voronoi Texture que da textura voronoi a los vasos sanguíneos de longitud más larga y el nodo ColorRamp
nodo_actual = nodos.new(type='NodeFrame')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.label = 'L'
nodo_actual.label_size = 20
nodo_actual.location = (-1763.4, 613.1)
nodo_actual.name = 'Frame_L'
nodo_actual.select = False
nodo_actual.width = 800

# Mapping_S el nodo mapping de los vasos sanguíneos de corta distancia es de tipo 'NORMAL' y la escala es de (1,2,1) haciendo referencia a (X,Y,Z)
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-33.8, -25.8)
nodo_actual.name = 'Mapping_S'
# Asignamos el nodo padre, ya que Mapping_S es un nodo que se encuentra en el interior de Frame_S
parent = nodos.get('Frame_S')
if parent:
    nodo_actual.parent = parent
    while True:
        nodo_actual.location += parent.location
        if parent.parent:
            parent = parent.parent
        else:
            break                    
nodo_actual.select = False
nodo_actual.vector_type = 'NORMAL'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 2.0, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Voronoi_Texture_M es el encargado de como vemos los vasos sanguíneos de longitud media
nodo_actual = nodos.new(type='ShaderNodeTexVoronoi')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.distance = 'EUCLIDEAN'
nodo_actual.feature = 'F1'
nodo_actual.location = (316.1, -30.7)
nodo_actual.name = 'Voronoi_Texture_M'
parent = nodos.get('Frame_M')
# Asignamos el nodo padre, ya que Voronoi_Texture_M es un nodo que se encuentra en el interior de Frame_M
if parent:
    nodo_actual.parent = parent
    while True:
        nodo_actual.location += parent.location
        if parent.parent:
            parent = parent.parent
        else:
            break                    
nodo_actual.select = False
nodo_actual.voronoi_dimensions = '3D'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = 6.0
nodo_actual.inputs[3].default_value = 1.0
nodo_actual.inputs[4].default_value = 0.5
nodo_actual.inputs[5].default_value = 1.0
nodo_actual.outputs[0].default_value = 0.0
nodo_actual.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.outputs[3].default_value = 0.0
nodo_actual.outputs[4].default_value = 0.0

# Mapping_M el nodo mapping de los vasos sanguíneos de distancia media es de tipo 'NORMAL' y la escala es de (1,2,1) haciendo referencia a (X,Y,Z)
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (4.8, -22.9)
nodo_actual.name = 'Mapping_M'
# Asignamos el nodo padre, ya que Mapping_M es un nodo que se encuentra en el interior del nodo de Frame_M
parent = nodos.get('Frame_M')
if parent:
    nodo_actual.parent = parent
    while True:
        nodo_actual.location += parent.location
        if parent.parent:
            parent = parent.parent
        else:
            break                    
nodo_actual.select = False
nodo_actual.vector_type = 'NORMAL'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 2.0, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# ColorRamp_M es el nodo encargado de proporcionar el color rojo a esos vasos sanguíneos de longitud media
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'
# creamos el punto que delimita la parte "más blanca"                
stop_actual = cr.elements.new(0.136)
# para crear el color blanco queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
# creamos el punto que delimita la parte "más roja"    
stop_actual = cr.elements.new(1.0)
# para crear el color rojo queremos en RGB los valores 0.314, 0.005, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.314, 0.005, 0.0, 1.0]
removed_black = removed_white = False
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (503.482, -26.962)
nodo_actual.name = 'ColorRamp_M'
# Asignamos el nodo padre, ya que ColorRamp_M es un nodo que se encuentra en el interior del nodo de Frame_M
parent = nodos.get('Frame_M')
if parent:
    nodo_actual.parent = parent
    while True:
        nodo_actual.location += parent.location
        if parent.parent:
            parent = parent.parent
        else:
            break                    
nodo_actual.select = False
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# ColorRamp_S es el nodo encargado de proporcionar el color rojo a esos vasos sanguíneos de longitud media
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'                
stop_actual = cr.elements.new(0.358)
# para crear el color blanco queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
stop_actual = cr.elements.new(1.0)
# para crear el color rojo queremos en RGB los valores 0.314, 0.005, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.314, 0.005, 0.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (464.786, -29.943)
nodo_actual.name = 'ColorRamp_S'
# Asignamos el nodo padre, ya que ColorRamp_S es un nodo que se encuentra en el interior del nodo de Frame_S
parent = nodos.get('Frame_S')
if parent:
    nodo_actual.parent = parent
    while True:
        nodo_actual.location += parent.location
        if parent.parent:
            parent = parent.parent
        else:
            break                    
nodo_actual.select = False
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Mix_M_L es el nodo encargado de mezclar los nodos colorRamp de M y de L con el tipo "DARKEN"
nodo_actual = nodos.new(type='ShaderNodeMixRGB')
nodo_actual.blend_type = 'DARKEN'
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-864.344, 929.187)
nodo_actual.name = 'Mix_M_L'
nodo_actual.select = False
nodo_actual.use_alpha = False
nodo_actual.use_clamp = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 1.0

# Mapping_L el nodo mapping de los vasos sanguíneos de corta distancia es de tipo 'NORMAL' y la escala es de (1,2,1) haciendo referencia a (X,Y,Z)
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-19.012, -46.767)
nodo_actual.name = 'Mapping_L'
# Asignamos el nodo padre, ya que Mapping_L es un nodo que se encuentra en el interior del nodo de Frame_L
parent = nodos.get('Frame_L')
if parent:
    nodo_actual.parent = parent
    while True:
        nodo_actual.location += parent.location
        if parent.parent:
            parent = parent.parent
        else:
            break                    
nodo_actual.select = False
nodo_actual.vector_type = 'NORMAL'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 4.0, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]
# Voronoi_Texture_L es el encargado de como vemos los vasos sanguíneos de larga longitud
nodo_actual = nodos.new(type='ShaderNodeTexVoronoi')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.distance = 'EUCLIDEAN'
nodo_actual.feature = 'F1'
nodo_actual.location = (292.31591796875, -54.62493896484375)
nodo_actual.name = 'Voronoi_Texture_L'
# Asignamos el nodo padre, ya que Mapping_L es un nodo que se encuentra en el interior del nodo de Frame_L
parent = nodos.get('Frame_L')
if parent:
    nodo_actual.parent = parent
    while True:
        nodo_actual.location += parent.location
        if parent.parent:
            parent = parent.parent
        else:
            break                    
nodo_actual.select = False
nodo_actual.voronoi_dimensions = '3D'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = 3.0
nodo_actual.inputs[3].default_value = 1.0
nodo_actual.inputs[4].default_value = 0.5
nodo_actual.inputs[5].default_value = 1.0
nodo_actual.outputs[0].default_value = 0.0
nodo_actual.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.outputs[3].default_value = 0.0
nodo_actual.outputs[4].default_value = 0.0

# Mix_S_ML es el nodo encargado de mezclar el nodo colorRampS con el nodo Mix_M_L con el tipo "DARKEN"
nodo_actual = nodos.new(type='ShaderNodeMixRGB')
nodo_actual.blend_type = 'DARKEN'
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-381.149, 1011.118)
nodo_actual.name = 'Mix_S_ML'
nodo_actual.select = False
nodo_actual.use_alpha = False
nodo_actual.use_clamp = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 0.300

# ColorRamp_Cornea es el nodo encargado de proporcionar el color blanco de la esclerótica y determina donde empieza el iris para que sea visible
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'                
stop_actual = cr.elements.new(0.579)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(0.607)
# para crear el color blanco queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-116.419, 161.154)
nodo_actual.name = 'ColorRamp_Cornea'
nodo_actual.select = False
nodo_actual.width = 143.66796875
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Mapping_Cornea sirve para dar esa transparencia necesaria para poder aprecias el iris/pupila del ojo
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-610.645, 158.537)
nodo_actual.name = 'Mapping_Cornea'
nodo_actual.select = False
nodo_actual.vector_type = 'POINT'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.800, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [0.5, 0.5, 0.5]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Gradient_Texture_Cornea sirve para dar esa transparencia necesaria para poder aprecias el iris/pupila del ojo, pues de estar en otro modo la transparencia no se situaría con esas dimensiones en la parte frontal
nodo_actual = nodos.new(type='ShaderNodeTexGradient')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.gradient_type = 'SPHERICAL'
nodo_actual.location = (-320.645, 96.098)
nodo_actual.name = 'Gradient_Texture_Cornea'
nodo_actual.select = False
nodo_actual.width = 140.0

# Gradient_Texture_Cornea sirve para dar esa transparencia necesaria para poder aprecias el iris/pupila del ojo,
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-820.645, 141.537)
nodo_actual.name = 'Texture_Coordinate_Cornea'
nodo_actual.object = None
nodo_actual.select = False
nodo_actual.width = 140.0

# Mapping_Iris_Superficie reflejará las líneas características del iris del ojo
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-742.519, 1637.214)
nodo_actual.name = 'Mapping_Iris_Superficie'
nodo_actual.select = False
nodo_actual.vector_type = 'POINT'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.800, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [0.5, 0.5, 0.5]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Gradient_Texture_Iris_Superficie es el nodo que muestrea la textura, al estar en modo esférico crea un degradado inverso utilizando el vector de Mapping_Iris_Superficie
nodo_actual = nodos.new(type='ShaderNodeTexGradient')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.gradient_type = 'SPHERICAL'
nodo_actual.location = (-452.5185546875, 1574.775634765625)
nodo_actual.name = 'Gradient_Texture_Iris_Superficie'
nodo_actual.select = False
nodo_actual.width = 140.0

# Texture_Coordinate_Iris_Superficie  utilizando las coordenadas del espacio objeto
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-952.5184326171875, 1620.214111328125)
nodo_actual.name = 'Texture_Coordinate_Iris_Superficie'
nodo_actual.object = None
nodo_actual.select = False
nodo_actual.width = 140.0

# Nodo para ver los vasos sanguíneos de la superfice del ojo ya que se mezcla con el nodo Mix_S_ML
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'EASE'                
stop_actual = cr.elements.new(0.455)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(0.577)
# para crear el color blanco queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-248.293, 1639.831)
nodo_actual.name = 'ColorRamp_Vasos_Sanguíneos'
nodo_actual.select = False
nodo_actual.width = 349.480
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Texture_Coordinate_S_M_L utilizando las coordenadas del espacio objeto el cual irá al nodo Mapping_S, Mapping_M y Mix_L el cual posteriormente la salida de color irá al nodo Mapping_L
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-2357.006, 985.429)
nodo_actual.name = 'Texture_Coordinate_S_M_L'
nodo_actual.object = None
nodo_actual.select = False
nodo_actual.width = 140.0

# Noise_Texture_L es un ruido 3D el cual le da ese efecto a los vasos sanguíneos 
nodo_actual = nodos.new(type='ShaderNodeTexNoise')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-2281.211, 671.236)
nodo_actual.name = 'Noise_Texture_L'
nodo_actual.noise_dimensions = '3D'
nodo_actual.select = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = 5.0
nodo_actual.inputs[3].default_value = 2.0
nodo_actual.inputs[4].default_value = 0.5
nodo_actual.inputs[5].default_value = 0.0
nodo_actual.outputs[0].default_value = 0.0
nodo_actual.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]

# Mix_L fusiona con el modo Luz Lineal entre Texture_Coordinate_S_M_L y el ruido 3D del Noise_Texture_L
nodo_actual = nodos.new(type='ShaderNodeMixRGB')
nodo_actual.blend_type = 'LINEAR_LIGHT'
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-2060.082, 661.099)
nodo_actual.name = 'Mix_L'
nodo_actual.select = False
nodo_actual.use_alpha = False
nodo_actual.use_clamp = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 0.30000001192092896
nodo_actual.inputs[1].default_value = [0.5, 0.5, 0.5, 1.0]
nodo_actual.inputs[2].default_value = [0.5, 0.5, 0.5, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

# ColorRamp_L es el nodo encargado de proporcionar el color rojo a esos vasos sanguíneos de longitud media
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'                
stop_actual = cr.elements.new(0.543)
# para crear el color BLANCO queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
stop_actual = cr.elements.new(0.848)
# para crear el color ROJO queremos en RGB los valores 0.314, 0.005 ,0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.314, 0.005, 0.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (475.047, -50.812)
nodo_actual.name = 'ColorRamp_L'
# Asignamos el nodo padre, ya que Mapping_L es un nodo que se encuentra en el interior del nodo de Frame_L
parent = nodos.get('Frame_L')
if parent:
    nodo_actual.parent = parent
    while True:
        nodo_actual.location += parent.location
        if parent.parent:
            parent = parent.parent
        else:
            break                    
nodo_actual.select = False
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0


# ColorRamp_Rojo_Superficie es el nodo encargado de poner un color rojo emulando a la sangre en la parte trasera del ojo aclarándose según avanza a la parte frontal del ojo además de delimitar donde terminan los vasos sanguíneos
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'EASE'                
stop_actual = cr.elements.new(0.091)
# para crear el color ROJO queremos en RGB los valores 0.314, 0.005 ,0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.314, 0.005, 0.0, 1.0]
stop_actual = cr.elements.new(0.347)
# para crear el color ROJO SUAVE queremos en RGB los valores 0.666, 0.264 ,0.174 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.666, 0.264, 0.174, 1.0]
stop_actual = cr.elements.new(0.611)
# para crear el color BLANCO queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-113.402, 384.835)
nodo_actual.name = 'ColorRamp_Rojo_Superficie'
nodo_actual.select = False
nodo_actual.width = 194.450
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Mix_Total es el nodo que mezcla de modo superpuesto todos los colorRamp relacionados con el rojo sanguíneo para mandarlo como color base al nodo principal BSDF
nodo_actual = nodos.new(type='ShaderNodeMixRGB')
nodo_actual.blend_type = 'OVERLAY'
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (629.845, 1025.724)
nodo_actual.name = 'Mix_Total'
nodo_actual.select = False
nodo_actual.use_alpha = False
nodo_actual.use_clamp = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 1.0
nodo_actual.inputs[1].default_value = [0.5, 0.5, 0.5, 1.0]
nodo_actual.inputs[2].default_value = [0.5, 0.5, 0.5, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

# Mix_Vasos_Sanguineos es el nodo que mezcla de modo superpuesto todos los colorRamp para dar una especie de altura a los vasos sanguíneos a través del nodo bump
nodo_actual = nodos.new(type='ShaderNodeMixRGB')
nodo_actual.blend_type = 'MIX'
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (54.530, 1012.599)
nodo_actual.name = 'Mix_Vasos_Sanguineos'
nodo_actual.select = False
nodo_actual.use_alpha = False
nodo_actual.use_clamp = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.inputs[1].default_value = [0.5, 0.5, 0.5, 1.0]
nodo_actual.inputs[2].default_value = [1.0, 1.0, 1.0, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]

# Bump es el nodo qotorga una especie de altura a los vasos sanguíneos a través del nodo bump
nodo_actual = nodos.new(type='ShaderNodeBump')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.invert = True
nodo_actual.location = (-65.068, -147.066)
nodo_actual.name = 'Bump'
nodo_actual.select = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 0.100
nodo_actual.inputs[1].default_value = 0.100
nodo_actual.inputs[2].default_value = 1.0
nodo_actual.inputs[3].default_value = [0.0, 0.0, 0.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# ColorRamp_Bump es el nodo qotorga color para esa sensación de altura que ofrece el nodo Bump
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'B_SPLINE'                
stop_actual = cr.elements.new(0.0)
# para crear el color NEGRO queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(1.0)
# para crear el color BLANCO queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-687.004, 647.723)
nodo_actual.name = 'ColorRamp_Bump'
nodo_actual.select = False
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0


# Voronoi_Texture_S es el encargado de como vemos los vasos sanguíneos de menor longitud
nodo_actual = nodos.new(type='ShaderNodeTexVoronoi')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.distance = 'EUCLIDEAN'
nodo_actual.feature = 'F1'
nodo_actual.location = (277.432, -33.755)
nodo_actual.name = 'Voronoi_Texture_S'
# Asignamos el nodo padre, ya que Mapping_L es un nodo que se encuentra en el interior del nodo de Frame_S
parent = nodos.get('Frame_S')
if parent:
    nodo_actual.parent = parent
    while True:
        nodo_actual.location += parent.location
        if parent.parent:
            parent = parent.parent
        else:
            break                    
nodo_actual.select = False
nodo_actual.voronoi_dimensions = '3D'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = 20.0
nodo_actual.inputs[3].default_value = 1.0
nodo_actual.inputs[4].default_value = 0.5
nodo_actual.inputs[5].default_value = 1.0
nodo_actual.outputs[0].default_value = 0.0
nodo_actual.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.outputs[3].default_value = 0.0
nodo_actual.outputs[4].default_value = 0.0

# Material Output es el nodo encargado de que todos los nodos hagan efecto en la superficie, sin él no se vería reflejado en la consola blender
nodo_actual = nodos.new(type='ShaderNodeOutputMaterial')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.is_active_output = True
nodo_actual.location = (576.799, 302.339)
nodo_actual.name = 'Material Output'
nodo_actual.select = False
nodo_actual.target = 'ALL'
nodo_actual.width = 140.0
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = 0.0

# Principled BSDF es el nodo que se crea por defecto en el cual se aplicará el nodo Mix_Total, Bump, y el ColorRamp_Vasos_Sanguíneos
nodo_actual = nodos.new(type='ShaderNodeBsdfPrincipled')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.distribution = 'GGX'
nodo_actual.location = (324.994, 311.986)
nodo_actual.name = 'Principled BSDF'
nodo_actual.subsurface_method = 'BURLEY'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.800, 0.800, 0.800, 1.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = [1.0, 0.200, 0.100]
nodo_actual.inputs[3].default_value = [0.800, 0.800, 0.800, 1.0]
nodo_actual.inputs[4].default_value = 1.399
nodo_actual.inputs[5].default_value = 0.0
nodo_actual.inputs[6].default_value = 0.0
nodo_actual.inputs[7].default_value = 0.5
nodo_actual.inputs[8].default_value = 0.0
nodo_actual.inputs[9].default_value = 0.0500
nodo_actual.inputs[10].default_value = 0.0
nodo_actual.inputs[11].default_value = 0.0
nodo_actual.inputs[12].default_value = 0.0
nodo_actual.inputs[13].default_value = 0.5
nodo_actual.inputs[14].default_value = 0.0
nodo_actual.inputs[15].default_value = 0.5
nodo_actual.inputs[16].default_value = 1.450
nodo_actual.inputs[17].default_value = 1.0
nodo_actual.inputs[18].default_value = 0.0
nodo_actual.inputs[19].default_value = [0.0, 0.0, 0.0, 1.0]
nodo_actual.inputs[20].default_value = 1.0
nodo_actual.inputs[21].default_value = 1.0
nodo_actual.inputs[22].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[23].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[24].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[25].default_value = 0.0

######### Enlaces entre los nodos #########

enlaces.new(nodos["Mapping_Cornea"].outputs[0], nodos["Gradient_Texture_Cornea"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Cornea"].outputs[3], nodos["Mapping_Cornea"].inputs[0])    
enlaces.new(nodos["Gradient_Texture_Cornea"].outputs[0], nodos["ColorRamp_Cornea"].inputs[0])    
enlaces.new(nodos["ColorRamp_Cornea"].outputs[0], nodos["Principled BSDF"].inputs[17])    
enlaces.new(nodos["Gradient_Texture_Cornea"].outputs[0], nodos["ColorRamp_Rojo_Superficie"].inputs[0])    
enlaces.new(nodos["Mapping_L"].outputs[0], nodos["Voronoi_Texture_L"].inputs[0])    
enlaces.new(nodos["Voronoi_Texture_L"].outputs[0], nodos["ColorRamp_L"].inputs[0])    
enlaces.new(nodos["Mapping_M"].outputs[0], nodos["Voronoi_Texture_M"].inputs[0])    
enlaces.new(nodos["Voronoi_Texture_M"].outputs[0], nodos["ColorRamp_M"].inputs[0])    
enlaces.new(nodos["Mapping_S"].outputs[0], nodos["Voronoi_Texture_S"].inputs[0])    
enlaces.new(nodos["Voronoi_Texture_S"].outputs[0], nodos["ColorRamp_S"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_S_M_L"].outputs[3], nodos["Mapping_M"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_S_M_L"].outputs[3], nodos["Mapping_S"].inputs[0])    
enlaces.new(nodos["ColorRamp_M"].outputs[0], nodos["Mix_M_L"].inputs[1])    
enlaces.new(nodos["ColorRamp_L"].outputs[0], nodos["Mix_M_L"].inputs[2])    
enlaces.new(nodos["Mix_M_L"].outputs[0], nodos["Mix_S_ML"].inputs[1])    
enlaces.new(nodos["ColorRamp_S"].outputs[0], nodos["Mix_S_ML"].inputs[2])    
enlaces.new(nodos["Mix_Total"].outputs[0], nodos["Principled BSDF"].inputs[0])    
enlaces.new(nodos["Mix_S_ML"].outputs[0], nodos["Mix_Vasos_Sanguineos"].inputs[1])    
enlaces.new(nodos["Mapping_Iris_Superficie"].outputs[0], nodos["Gradient_Texture_Iris_Superficie"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Iris_Superficie"].outputs[3], nodos["Mapping_Iris_Superficie"].inputs[0])    
enlaces.new(nodos["Gradient_Texture_Iris_Superficie"].outputs[0], nodos["ColorRamp_Vasos_Sanguíneos"].inputs[0])    
enlaces.new(nodos["ColorRamp_Vasos_Sanguíneos"].outputs[0], nodos["Mix_Vasos_Sanguineos"].inputs[0])    
enlaces.new(nodos["Mix_Vasos_Sanguineos"].outputs[0], nodos["Mix_Total"].inputs[2])    
enlaces.new(nodos["ColorRamp_Rojo_Superficie"].outputs[0], nodos["Mix_Total"].inputs[1])    
enlaces.new(nodos["Noise_Texture_L"].outputs[1], nodos["Mix_L"].inputs[2])    
enlaces.new(nodos["Texture_Coordinate_S_M_L"].outputs[3], nodos["Mix_L"].inputs[1])    
enlaces.new(nodos["Mix_L"].outputs[0], nodos["Mapping_L"].inputs[0])    
enlaces.new(nodos["Mix_Vasos_Sanguineos"].outputs[0], nodos["ColorRamp_Bump"].inputs[0])    
enlaces.new(nodos["ColorRamp_Bump"].outputs[0], nodos["Bump"].inputs[2])    
enlaces.new(nodos["Bump"].outputs[0], nodos["Principled BSDF"].inputs[22])    
enlaces.new(nodos["Principled BSDF"].outputs[0], nodos["Material Output"].inputs[0])    

####################################################################### Iris_Azul_2 #######################################################################
obj = bpy.context.object  # Asignación de la mesh seleccionada con el puntero

new_mat = bpy.data.materials.get('Iris_Azul_2')
if not new_mat:
    new_mat = bpy.data.materials.new('Iris_Azul_2')
    
# Activamos las refracción para poder ver la pupila
bpy.context.object.active_material.use_screen_refraction = True

# habilitaremos el uso de nodos, ya que sin ello no podríamos crear ninguno
new_mat.use_nodes = True

# Definimos la estructura que tendran los nodos y los enlaces para su creación
node_tree = new_mat.node_tree
nodos = node_tree.nodes
nodos.clear()
    
enlaces = node_tree.links
enlaces.clear()
    
######### Nodos #########


# Mapping_Pupila determina el radio de la pupila
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-760.619, 177.171)
nodo_actual.name = 'Mapping_Pupila'
nodo_actual.vector_type = 'POINT'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.649, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 1.0, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Gradient_Texture_Iris_Medida es el nodo que muestrea la textura, al estar en modo esférico crea un degradado inverso utilizando el vector de Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexGradient')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.gradient_type = 'SPHERICAL'
nodo_actual.location = (-470.620, 115.160)
nodo_actual.name = 'Gradient_Texture_Iris_Medida'
nodo_actual.width = 140.0

# Texture_Coordinate_Iris_Base utilizando las coordenadas del espacio objeto el cual irá al nodo Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-970.619, 160.171)
nodo_actual.name = 'Texture_Coordinate_Iris_Base'
nodo_actual.object = None
nodo_actual.width = 140.0

# Texture_Coordinate_Iris_Interior utilizando las coordenadas del espacio objeto el cual irá al nodo Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-987.080, 524.705)
nodo_actual.name = 'Texture_Coordinate_Iris_Interior'
nodo_actual.object = None
nodo_actual.width = 140.0

# Mapping_Iris es el nodo utilizado para las "líneas" del Iris
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-777.080, 541.705)
nodo_actual.name = 'Mapping_Iris'
nodo_actual.vector_type = 'NORMAL'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 15.600, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Noise_Texture_Iris es el nodo que trata la distorsión y lo nítido que es el Iris
nodo_actual = nodos.new(type='ShaderNodeTexNoise')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-480.180, 462.844)
nodo_actual.name = 'Noise_Texture_Iris'
nodo_actual.noise_dimensions = '3D'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = 5.0
nodo_actual.inputs[3].default_value = 10.0
nodo_actual.inputs[4].default_value = 0.5
nodo_actual.inputs[5].default_value = 2.5
nodo_actual.outputs[0].default_value = 0.0
nodo_actual.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]

# ColorRamp_Iris_Interior es el nodo encargado de las tonalidades de azul en el interior del iris
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'
stop_actual = cr.elements.new(0.350)
# para crear el color azul claro queremos en RGB los valores 0.117, 0.250, 0.328 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.117, 0.250, 0.328, 1.0]
stop_actual = cr.elements.new(0.600)
# para crear el color azul oscuro queremos en RGB los valores 0.109, 0.141, 0.175 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.109, 0.141, 0.175, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-235.032, 521.752)
nodo_actual.name = 'ColorRamp_Iris_Interior'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# ColorRamp_Iris_Circunferencia es el nodo encargado de las tonalidades de azul en el interior del iris
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'EASE'                
stop_actual = cr.elements.new(0.5)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(0.550)
# para crear el color azul amarronado oscuro queremos en RGB los valores 0.100, 0.141, 0.238 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.100, 0.141, 0.238, 1.0]
stop_actual = cr.elements.new(0.620)
# para crear el color azul amarronado oscuro pálido queremos en RGB los valores 0.120, 0.258, 0.356 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.120, 0.258, 0.356, 1.0]
stop_actual = cr.elements.new(0.700)
# para crear el color azul amarronado claro queremos en RGB los valores 0.100, 0.227, 0.301 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.100, 0.227, 0.301, 1.0]
stop_actual = cr.elements.new(0.760)
# para crear el color azul oscuro pálido queremos en RGB los valores 0.156, 0.130, 0.068 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.156, 0.130, 0.068, 1.0]
stop_actual = cr.elements.new(0.764)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-237.990, 246.606)
nodo_actual.name = 'ColorRamp_Iris_Circunferencia'
nodo_actual.width = 244.526
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Mix es el nodo que mezcla de modo superpuesto ColorRamp_Iris_Interior con ColorRamp_Iris_Circunferencia para dar ese patrón al iris 
nodo_actual = nodos.new(type='ShaderNodeMixRGB')
nodo_actual.blend_type = 'OVERLAY'
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (281.812, 481.425)
nodo_actual.name = 'Mix'
nodo_actual.use_alpha = False
nodo_actual.use_clamp = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 1.0

# Material Output es el nodo encargado de que todos los nodos hagan efecto en la mesh, sin él no se vería reflejado en la aplicación de Blender
nodo_actual = nodos.new(type='ShaderNodeOutputMaterial')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.is_active_output = True
nodo_actual.location = (1551.203, 451.363)
nodo_actual.name = 'Material Output'
nodo_actual.target = 'ALL'
nodo_actual.width = 140.0
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = 0.0

# Principled BSDF es el nodo que se crea por defecto en el cual se aplicará el nodo Mix en el color Base y el Bump para la nitidez del iris
nodo_actual = nodos.new(type='ShaderNodeBsdfPrincipled')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.distribution = 'GGX'
nodo_actual.location = (1213.195, 444.630)
nodo_actual.name = 'Principled BSDF'
nodo_actual.subsurface_method = 'BURLEY'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.008, 0.0, 0.800, 1.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = [1.0, 0.200, 0.100]
nodo_actual.inputs[3].default_value = [0.800, 0.800, 0.800, 1.0]
nodo_actual.inputs[4].default_value = 1.399
nodo_actual.inputs[5].default_value = 0.0
nodo_actual.inputs[6].default_value = 0.699
nodo_actual.inputs[7].default_value = 0.0
nodo_actual.inputs[8].default_value = 0.0
nodo_actual.inputs[9].default_value = 0.5
nodo_actual.inputs[10].default_value = 0.0
nodo_actual.inputs[11].default_value = 0.0
nodo_actual.inputs[12].default_value = 0.0
nodo_actual.inputs[13].default_value = 0.5
nodo_actual.inputs[14].default_value = 0.0
nodo_actual.inputs[15].default_value = 0.029
nodo_actual.inputs[16].default_value = 1.450
nodo_actual.inputs[17].default_value = 0.0
nodo_actual.inputs[18].default_value = 0.0
nodo_actual.inputs[19].default_value = [0.0, 0.0, 0.0, 1.0]
nodo_actual.inputs[20].default_value = 1.0
nodo_actual.inputs[21].default_value = 1.0
nodo_actual.inputs[22].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[23].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[24].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[25].default_value = 0.0

# ColorRamp_Iris_Textura es el nodo encargado de las tonalidades del iris internas
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'                
stop_actual = cr.elements.new(0.050)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(1.0)
# para crear el color blanco queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (523.012, 309.724)
nodo_actual.name = 'ColorRamp_Iris_Textura'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Bump es el nodo qotorga una especie de altura a las líneas que determinan el patrón del Iris
nodo_actual = nodos.new(type='ShaderNodeBump')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.invert = False
nodo_actual.location = (931.314, 292.384)
nodo_actual.name = 'Bump'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 0.100
nodo_actual.inputs[1].default_value = 0.100
nodo_actual.inputs[2].default_value = 1.0
nodo_actual.inputs[3].default_value = [0.0, 0.0, 0.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

######### Enlaces entre los nodos #########

enlaces.new(nodos["Mapping_Pupila"].outputs[0], nodos["Gradient_Texture_Iris_Medida"].inputs[0])    
enlaces.new(nodos["Gradient_Texture_Iris_Medida"].outputs[0], nodos["ColorRamp_Iris_Circunferencia"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Iris_Base"].outputs[3], nodos["Mapping_Pupila"].inputs[0])    
enlaces.new(nodos["Mapping_Iris"].outputs[0], nodos["Noise_Texture_Iris"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Iris_Interior"].outputs[3], nodos["Mapping_Iris"].inputs[0])    
enlaces.new(nodos["Noise_Texture_Iris"].outputs[0], nodos["ColorRamp_Iris_Interior"].inputs[0])    
enlaces.new(nodos["ColorRamp_Iris_Circunferencia"].outputs[0], nodos["Mix"].inputs[1])    
enlaces.new(nodos["ColorRamp_Iris_Interior"].outputs[0], nodos["Mix"].inputs[2])    
enlaces.new(nodos["Mix"].outputs[0], nodos["Principled BSDF"].inputs[0])    
enlaces.new(nodos["Mix"].outputs[0], nodos["ColorRamp_Iris_Textura"].inputs[0])    
enlaces.new(nodos["Principled BSDF"].outputs[0], nodos["Material Output"].inputs[0])    
enlaces.new(nodos["ColorRamp_Iris_Textura"].outputs[0], nodos["Bump"].inputs[2])    
enlaces.new(nodos["Bump"].outputs[0], nodos["Principled BSDF"].inputs[22])    

import bpy

####################################################################### Iris_Azul #######################################################################
obj = bpy.context.object  # Asignación de la mesh seleccionada con el puntero

new_mat = bpy.data.materials.get('Iris_Azul')
if not new_mat:
    new_mat = bpy.data.materials.new('Iris_Azul')
    
# Activamos las refracción para poder ver la pupila
bpy.context.object.active_material.use_screen_refraction = True

# habilitaremos el uso de nodos, ya que sin ello no podríamos crear ninguno
new_mat.use_nodes = True

# Definimos la estructura que tendran los nodos y los enlaces para su creación
node_tree = new_mat.node_tree
nodos = node_tree.nodes
nodos.clear()
    
enlaces = node_tree.links
enlaces.clear()
    
######### Nodos #########


# Mapping_Pupila determina el radio de la pupila
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-760.619, 177.171)
nodo_actual.name = 'Mapping_Pupila'
nodo_actual.vector_type = 'POINT'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.649, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 1.0, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Gradient_Texture_Iris_Medida es el nodo que muestrea la textura, al estar en modo esférico crea un degradado inverso utilizando el vector de Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexGradient')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.gradient_type = 'SPHERICAL'
nodo_actual.location = (-470.620, 115.160)
nodo_actual.name = 'Gradient_Texture_Iris_Medida'
nodo_actual.width = 140.0

# Texture_Coordinate_Iris_Base utilizando las coordenadas del espacio objeto el cual irá al nodo Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-970.619, 160.171)
nodo_actual.name = 'Texture_Coordinate_Iris_Base'
nodo_actual.object = None
nodo_actual.width = 140.0

# Texture_Coordinate_Iris_Interior utilizando las coordenadas del espacio objeto el cual irá al nodo Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-987.080, 524.705)
nodo_actual.name = 'Texture_Coordinate_Iris_Interior'
nodo_actual.object = None
nodo_actual.width = 140.0

# Mapping_Iris es el nodo utilizado para las "líneas" del Iris
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-777.080, 541.705)
nodo_actual.name = 'Mapping_Iris'
nodo_actual.vector_type = 'NORMAL'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 15.600, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Noise_Texture_Iris es el nodo que trata la distorsión y lo nítido que es el Iris
nodo_actual = nodos.new(type='ShaderNodeTexNoise')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-480.180, 462.844)
nodo_actual.name = 'Noise_Texture_Iris'
nodo_actual.noise_dimensions = '3D'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = 5.0
nodo_actual.inputs[3].default_value = 10.0
nodo_actual.inputs[4].default_value = 0.5
nodo_actual.inputs[5].default_value = 2.5
nodo_actual.outputs[0].default_value = 0.0
nodo_actual.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]

# ColorRamp_Iris_Interior es el nodo encargado de las tonalidades de azul en el interior del iris
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'
stop_actual = cr.elements.new(0.350)
# para crear el color azul claro queremos en RGB los valores 0.318, 0.462, 0.474 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.318, 0.462, 0.474, 1.0]
stop_actual = cr.elements.new(0.600)
# para crear el color azul oscuro queremos en RGB los valores 0.093, 0.188, 0.195 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.093, 0.188, 0.195, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-235.032, 521.752)
nodo_actual.name = 'ColorRamp_Iris_Interior'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# ColorRamp_Iris_Circunferencia es el nodo encargado de las tonalidades de azul en el interior del iris
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'EASE'                
stop_actual = cr.elements.new(0.5)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(0.550)
# para crear el color azul amarronado oscuro queremos en RGB los valores 0.040, 0.117, 0.139 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.040, 0.117, 0.139, 1.0]
stop_actual = cr.elements.new(0.620)
# para crear el color azul amarronado oscuro pálido queremos en RGB los valores 0.014, 0.279, 0.287 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.014, 0.279, 0.287, 1.0]
stop_actual = cr.elements.new(0.700)
# para crear el color azul amarronado claro queremos en RGB los valores 0.109, 0.212, 0.235 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.109, 0.212, 0.235, 1.0]
stop_actual = cr.elements.new(0.760)
# para crear el color azul oscuro pálido queremos en RGB los valores 0.019, 0.089, 0.105 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.019, 0.089, 0.105, 1.0]
stop_actual = cr.elements.new(0.764)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-237.990, 246.606)
nodo_actual.name = 'ColorRamp_Iris_Circunferencia'
nodo_actual.width = 244.526
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Mix es el nodo que mezcla de modo superpuesto ColorRamp_Iris_Interior con ColorRamp_Iris_Circunferencia para dar ese patrón al iris 
nodo_actual = nodos.new(type='ShaderNodeMixRGB')
nodo_actual.blend_type = 'OVERLAY'
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (281.812, 481.425)
nodo_actual.name = 'Mix'
nodo_actual.use_alpha = False
nodo_actual.use_clamp = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 1.0

# Material Output es el nodo encargado de que todos los nodos hagan efecto en la mesh, sin él no se vería reflejado en la aplicación de Blender
nodo_actual = nodos.new(type='ShaderNodeOutputMaterial')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.is_active_output = True
nodo_actual.location = (1551.203, 451.363)
nodo_actual.name = 'Material Output'
nodo_actual.target = 'ALL'
nodo_actual.width = 140.0
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = 0.0

# Principled BSDF es el nodo que se crea por defecto en el cual se aplicará el nodo Mix en el color Base y el Bump para la nitidez del iris
nodo_actual = nodos.new(type='ShaderNodeBsdfPrincipled')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.distribution = 'GGX'
nodo_actual.location = (1213.195, 444.630)
nodo_actual.name = 'Principled BSDF'
nodo_actual.subsurface_method = 'BURLEY'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.008, 0.0, 0.800, 1.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = [1.0, 0.200, 0.100]
nodo_actual.inputs[3].default_value = [0.800, 0.800, 0.800, 1.0]
nodo_actual.inputs[4].default_value = 1.399
nodo_actual.inputs[5].default_value = 0.0
nodo_actual.inputs[6].default_value = 0.699
nodo_actual.inputs[7].default_value = 0.0
nodo_actual.inputs[8].default_value = 0.0
nodo_actual.inputs[9].default_value = 0.5
nodo_actual.inputs[10].default_value = 0.0
nodo_actual.inputs[11].default_value = 0.0
nodo_actual.inputs[12].default_value = 0.0
nodo_actual.inputs[13].default_value = 0.5
nodo_actual.inputs[14].default_value = 0.0
nodo_actual.inputs[15].default_value = 0.029
nodo_actual.inputs[16].default_value = 1.450
nodo_actual.inputs[17].default_value = 0.0
nodo_actual.inputs[18].default_value = 0.0
nodo_actual.inputs[19].default_value = [0.0, 0.0, 0.0, 1.0]
nodo_actual.inputs[20].default_value = 1.0
nodo_actual.inputs[21].default_value = 1.0
nodo_actual.inputs[22].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[23].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[24].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[25].default_value = 0.0

# ColorRamp_Iris_Textura es el nodo encargado de las tonalidades del iris internas
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'                
stop_actual = cr.elements.new(0.050)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(1.0)
# para crear el color blanco queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (523.012, 309.724)
nodo_actual.name = 'ColorRamp_Iris_Textura'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Bump es el nodo qotorga una especie de altura a las líneas que determinan el patrón del Iris
nodo_actual = nodos.new(type='ShaderNodeBump')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.invert = False
nodo_actual.location = (931.314, 292.384)
nodo_actual.name = 'Bump'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 0.100
nodo_actual.inputs[1].default_value = 0.100
nodo_actual.inputs[2].default_value = 1.0
nodo_actual.inputs[3].default_value = [0.0, 0.0, 0.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

######### Enlaces entre los nodos #########

enlaces.new(nodos["Mapping_Pupila"].outputs[0], nodos["Gradient_Texture_Iris_Medida"].inputs[0])    
enlaces.new(nodos["Gradient_Texture_Iris_Medida"].outputs[0], nodos["ColorRamp_Iris_Circunferencia"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Iris_Base"].outputs[3], nodos["Mapping_Pupila"].inputs[0])    
enlaces.new(nodos["Mapping_Iris"].outputs[0], nodos["Noise_Texture_Iris"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Iris_Interior"].outputs[3], nodos["Mapping_Iris"].inputs[0])    
enlaces.new(nodos["Noise_Texture_Iris"].outputs[0], nodos["ColorRamp_Iris_Interior"].inputs[0])    
enlaces.new(nodos["ColorRamp_Iris_Circunferencia"].outputs[0], nodos["Mix"].inputs[1])    
enlaces.new(nodos["ColorRamp_Iris_Interior"].outputs[0], nodos["Mix"].inputs[2])    
enlaces.new(nodos["Mix"].outputs[0], nodos["Principled BSDF"].inputs[0])    
enlaces.new(nodos["Mix"].outputs[0], nodos["ColorRamp_Iris_Textura"].inputs[0])    
enlaces.new(nodos["Principled BSDF"].outputs[0], nodos["Material Output"].inputs[0])    
enlaces.new(nodos["ColorRamp_Iris_Textura"].outputs[0], nodos["Bump"].inputs[2])    
enlaces.new(nodos["Bump"].outputs[0], nodos["Principled BSDF"].inputs[22])    

import bpy

####################################################################### Iris_Marron #######################################################################
obj = bpy.context.object  # Asignación de la mesh seleccionada con el puntero

new_mat = bpy.data.materials.get('Iris_Marron')
if not new_mat:
    new_mat = bpy.data.materials.new('Iris_Marron')
    
# Activamos las refracción para poder ver la pupila
bpy.context.object.active_material.use_screen_refraction = True

# habilitaremos el uso de nodos, ya que sin ello no podríamos crear ninguno
new_mat.use_nodes = True

# Definimos la estructura que tendran los nodos y los enlaces para su creación
node_tree = new_mat.node_tree
nodos = node_tree.nodes
nodos.clear()
    
enlaces = node_tree.links
enlaces.clear()
    
######### Nodos #########


# Mapping_Pupila determina el radio de la pupila
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-760.619, 177.171)
nodo_actual.name = 'Mapping_Pupila'
nodo_actual.vector_type = 'POINT'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.649, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 1.0, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Gradient_Texture_Iris_Medida es el nodo que muestrea la textura, al estar en modo esférico crea un degradado inverso utilizando el vector de Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexGradient')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.gradient_type = 'SPHERICAL'
nodo_actual.location = (-470.620, 115.160)
nodo_actual.name = 'Gradient_Texture_Iris_Medida'
nodo_actual.width = 140.0

# Texture_Coordinate_Iris_Base utilizando las coordenadas del espacio objeto el cual irá al nodo Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-970.619, 160.171)
nodo_actual.name = 'Texture_Coordinate_Iris_Base'
nodo_actual.object = None
nodo_actual.width = 140.0

# Texture_Coordinate_Iris_Interior utilizando las coordenadas del espacio objeto el cual irá al nodo Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-987.080, 524.705)
nodo_actual.name = 'Texture_Coordinate_Iris_Interior'
nodo_actual.object = None
nodo_actual.width = 140.0

# Mapping_Iris es el nodo utilizado para las "líneas" del Iris
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-777.080, 541.705)
nodo_actual.name = 'Mapping_Iris'
nodo_actual.vector_type = 'NORMAL'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 15.600, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Noise_Texture_Iris es el nodo que trata la distorsión y lo nítido que es el Iris
nodo_actual = nodos.new(type='ShaderNodeTexNoise')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-480.180, 462.844)
nodo_actual.name = 'Noise_Texture_Iris'
nodo_actual.noise_dimensions = '3D'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = 5.0
nodo_actual.inputs[3].default_value = 10.0
nodo_actual.inputs[4].default_value = 0.5
nodo_actual.inputs[5].default_value = 2.5
nodo_actual.outputs[0].default_value = 0.0
nodo_actual.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]

# ColorRamp_Iris_Interior es el nodo encargado de las tonalidades de azul en el interior del iris
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'
stop_actual = cr.elements.new(0.350)
# para crear el color marrón claro queremos en RGB los valores 0.342, 0.164, 0.104 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.342, 0.164, 0.104, 1.0]
stop_actual = cr.elements.new(0.600)
# para crear el color marrón oscuro queremos en RGB los valores 0.205, 0.073, 0.046 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.205, 0.073, 0.046, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-235.032, 521.752)
nodo_actual.name = 'ColorRamp_Iris_Interior'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# ColorRamp_Iris_Circunferencia es el nodo encargado de las tonalidades de azul en el interior del iris
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'EASE'                
stop_actual = cr.elements.new(0.5)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(0.550)
# para crear el color marrón amarronado oscuro queremos en RGB los valores 0.182, 0.136, 0.127 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.182, 0.136, 0.127, 1.0]
stop_actual = cr.elements.new(0.620)
# para crear el color marrón amarronado oscuro pálido queremos en RGB los valores 0.175, 0.070, 0.024 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.175, 0.070, 0.024, 1.0]
stop_actual = cr.elements.new(0.700)
# para crear el color marrón amarronado claro queremos en RGB los valores 0.133, 0.037, 0.002 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.133, 0.037, 0.002, 1.0]
stop_actual = cr.elements.new(0.760)
# para crear el color marrón oscuro pálido queremos en RGB los valores 0.133, 0.037, 0.002 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.133, 0.037, 0.002, 1.0]
stop_actual = cr.elements.new(0.764)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-237.990, 246.606)
nodo_actual.name = 'ColorRamp_Iris_Circunferencia'
nodo_actual.width = 244.526
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Mix es el nodo que mezcla de modo superpuesto ColorRamp_Iris_Interior con ColorRamp_Iris_Circunferencia para dar ese patrón al iris 
nodo_actual = nodos.new(type='ShaderNodeMixRGB')
nodo_actual.blend_type = 'OVERLAY'
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (281.812, 481.425)
nodo_actual.name = 'Mix'
nodo_actual.use_alpha = False
nodo_actual.use_clamp = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 1.0

# Material Output es el nodo encargado de que todos los nodos hagan efecto en la mesh, sin él no se vería reflejado en la aplicación de Blender
nodo_actual = nodos.new(type='ShaderNodeOutputMaterial')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.is_active_output = True
nodo_actual.location = (1551.203, 451.363)
nodo_actual.name = 'Material Output'
nodo_actual.target = 'ALL'
nodo_actual.width = 140.0
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = 0.0

# Principled BSDF es el nodo que se crea por defecto en el cual se aplicará el nodo Mix en el color Base y el Bump para la nitidez del iris
nodo_actual = nodos.new(type='ShaderNodeBsdfPrincipled')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.distribution = 'GGX'
nodo_actual.location = (1213.195, 444.630)
nodo_actual.name = 'Principled BSDF'
nodo_actual.subsurface_method = 'BURLEY'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.008, 0.0, 0.800, 1.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = [1.0, 0.200, 0.100]
nodo_actual.inputs[3].default_value = [0.800, 0.800, 0.800, 1.0]
nodo_actual.inputs[4].default_value = 1.399
nodo_actual.inputs[5].default_value = 0.0
nodo_actual.inputs[6].default_value = 0.699
nodo_actual.inputs[7].default_value = 0.0
nodo_actual.inputs[8].default_value = 0.0
nodo_actual.inputs[9].default_value = 0.5
nodo_actual.inputs[10].default_value = 0.0
nodo_actual.inputs[11].default_value = 0.0
nodo_actual.inputs[12].default_value = 0.0
nodo_actual.inputs[13].default_value = 0.5
nodo_actual.inputs[14].default_value = 0.0
nodo_actual.inputs[15].default_value = 0.029
nodo_actual.inputs[16].default_value = 1.450
nodo_actual.inputs[17].default_value = 0.0
nodo_actual.inputs[18].default_value = 0.0
nodo_actual.inputs[19].default_value = [0.0, 0.0, 0.0, 1.0]
nodo_actual.inputs[20].default_value = 1.0
nodo_actual.inputs[21].default_value = 1.0
nodo_actual.inputs[22].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[23].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[24].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[25].default_value = 0.0

# ColorRamp_Iris_Textura es el nodo encargado de las tonalidades del iris internas
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'                
stop_actual = cr.elements.new(0.050)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(1.0)
# para crear el color blanco queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (523.012, 309.724)
nodo_actual.name = 'ColorRamp_Iris_Textura'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Bump es el nodo qotorga una especie de altura a las líneas que determinan el patrón del Iris
nodo_actual = nodos.new(type='ShaderNodeBump')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.invert = False
nodo_actual.location = (931.314, 292.384)
nodo_actual.name = 'Bump'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 0.100
nodo_actual.inputs[1].default_value = 0.100
nodo_actual.inputs[2].default_value = 1.0
nodo_actual.inputs[3].default_value = [0.0, 0.0, 0.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

######### Enlaces entre los nodos #########

enlaces.new(nodos["Mapping_Pupila"].outputs[0], nodos["Gradient_Texture_Iris_Medida"].inputs[0])    
enlaces.new(nodos["Gradient_Texture_Iris_Medida"].outputs[0], nodos["ColorRamp_Iris_Circunferencia"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Iris_Base"].outputs[3], nodos["Mapping_Pupila"].inputs[0])    
enlaces.new(nodos["Mapping_Iris"].outputs[0], nodos["Noise_Texture_Iris"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Iris_Interior"].outputs[3], nodos["Mapping_Iris"].inputs[0])    
enlaces.new(nodos["Noise_Texture_Iris"].outputs[0], nodos["ColorRamp_Iris_Interior"].inputs[0])    
enlaces.new(nodos["ColorRamp_Iris_Circunferencia"].outputs[0], nodos["Mix"].inputs[1])    
enlaces.new(nodos["ColorRamp_Iris_Interior"].outputs[0], nodos["Mix"].inputs[2])    
enlaces.new(nodos["Mix"].outputs[0], nodos["Principled BSDF"].inputs[0])    
enlaces.new(nodos["Mix"].outputs[0], nodos["ColorRamp_Iris_Textura"].inputs[0])    
enlaces.new(nodos["Principled BSDF"].outputs[0], nodos["Material Output"].inputs[0])    
enlaces.new(nodos["ColorRamp_Iris_Textura"].outputs[0], nodos["Bump"].inputs[2])    
enlaces.new(nodos["Bump"].outputs[0], nodos["Principled BSDF"].inputs[22])    

import bpy

####################################################################### Iris_Verde #######################################################################
obj = bpy.context.object  # Asignación de la mesh seleccionada con el puntero

new_mat = bpy.data.materials.get('Iris_Verde')
if not new_mat:
    new_mat = bpy.data.materials.new('Iris_Verde')
    
# Activamos las refracción para poder ver la pupila
bpy.context.object.active_material.use_screen_refraction = True

# habilitaremos el uso de nodos, ya que sin ello no podríamos crear ninguno
new_mat.use_nodes = True

# Definimos la estructura que tendran los nodos y los enlaces para su creación
node_tree = new_mat.node_tree
nodos = node_tree.nodes
nodos.clear()
    
enlaces = node_tree.links
enlaces.clear()
    
######### Nodos #########

# Mapping_Pupila determina el radio de la pupila
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-760.619, 177.171)
nodo_actual.name = 'Mapping_Pupila'
nodo_actual.vector_type = 'POINT'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.649, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 1.0, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Gradient_Texture_Iris_Medida es el nodo que muestrea la textura, al estar en modo esférico crea un degradado inverso utilizando el vector de Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexGradient')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.gradient_type = 'SPHERICAL'
nodo_actual.location = (-470.620, 115.160)
nodo_actual.name = 'Gradient_Texture_Iris_Medida'
nodo_actual.width = 140.0

# Texture_Coordinate_Iris_Base utilizando las coordenadas del espacio objeto el cual irá al nodo Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-970.619, 160.171)
nodo_actual.name = 'Texture_Coordinate_Iris_Base'
nodo_actual.object = None
nodo_actual.width = 140.0

# Texture_Coordinate_Iris_Interior utilizando las coordenadas del espacio objeto el cual irá al nodo Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-987.080, 524.705)
nodo_actual.name = 'Texture_Coordinate_Iris_Interior'
nodo_actual.object = None
nodo_actual.width = 140.0

# Mapping_Iris es el nodo utilizado para las "líneas" del Iris
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-777.080, 541.705)
nodo_actual.name = 'Mapping_Iris'
nodo_actual.vector_type = 'NORMAL'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 15.600, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Noise_Texture_Iris es el nodo que trata la distorsión y lo nítido que es el Iris
nodo_actual = nodos.new(type='ShaderNodeTexNoise')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-480.180, 462.844)
nodo_actual.name = 'Noise_Texture_Iris'
nodo_actual.noise_dimensions = '3D'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = 5.0
nodo_actual.inputs[3].default_value = 10.0
nodo_actual.inputs[4].default_value = 0.5
nodo_actual.inputs[5].default_value = 2.5
nodo_actual.outputs[0].default_value = 0.0
nodo_actual.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]

# ColorRamp_Iris_Interior es el nodo encargado de las tonalidades de azul en el interior del iris
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'
stop_actual = cr.elements.new(0.350)
# para crear el color verde claro queremos en RGB los valores 0.342, 0.274 0.202 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.342, 0.274, 0.202, 1.0]
stop_actual = cr.elements.new(0.600)
# para crear el color verde oscuro queremos en RGB los valores 0.235, 0.209, 0.175 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.235, 0.209, 0.175, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-235.032, 521.752)
nodo_actual.name = 'ColorRamp_Iris_Interior'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# ColorRamp_Iris_Circunferencia es el nodo encargado de las tonalidades de azul en el interior del iris
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'EASE'                
stop_actual = cr.elements.new(0.5)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(0.550)
# para crear el color verde amarronado oscuro queremos en RGB los valores 0.154, 0.116, 0.086 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.154, 0.116, 0.086, 1.0]
stop_actual = cr.elements.new(0.620)
# para crear el color verde amarronado oscuro pálido queremos en RGB los valores 0.319, 0.287, 0.254 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.319, 0.287, 0.254, 1.0]
stop_actual = cr.elements.new(0.700)
# para crear el color verde amarronado claro queremos en RGB los valores 0.279, 0.266, 0.238 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.279, 0.266, 0.238, 1.0]
stop_actual = cr.elements.new(0.760)
# para crear el color marrón oscuro pálido queremos en RGB los valores 0.181, 0.107, 0.100 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.181, 0.107, 0.100, 1.0]
stop_actual = cr.elements.new(0.764)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-237.990, 246.606)
nodo_actual.name = 'ColorRamp_Iris_Circunferencia'
nodo_actual.width = 244.526
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Mix es el nodo que mezcla de modo superpuesto ColorRamp_Iris_Interior con ColorRamp_Iris_Circunferencia para dar ese patrón al iris 
nodo_actual = nodos.new(type='ShaderNodeMixRGB')
nodo_actual.blend_type = 'OVERLAY'
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (281.812, 481.425)
nodo_actual.name = 'Mix'
nodo_actual.use_alpha = False
nodo_actual.use_clamp = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 1.0

# Material Output es el nodo encargado de que todos los nodos hagan efecto en la mesh, sin él no se vería reflejado en la aplicación de Blender
nodo_actual = nodos.new(type='ShaderNodeOutputMaterial')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.is_active_output = True
nodo_actual.location = (1551.203, 451.363)
nodo_actual.name = 'Material Output'
nodo_actual.target = 'ALL'
nodo_actual.width = 140.0
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = 0.0

# Principled BSDF es el nodo que se crea por defecto en el cual se aplicará el nodo Mix en el color Base y el Bump para la nitidez del iris
nodo_actual = nodos.new(type='ShaderNodeBsdfPrincipled')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.distribution = 'GGX'
nodo_actual.location = (1213.195, 444.630)
nodo_actual.name = 'Principled BSDF'
nodo_actual.subsurface_method = 'BURLEY'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.008, 0.0, 0.800, 1.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = [1.0, 0.200, 0.100]
nodo_actual.inputs[3].default_value = [0.800, 0.800, 0.800, 1.0]
nodo_actual.inputs[4].default_value = 1.399
nodo_actual.inputs[5].default_value = 0.0
nodo_actual.inputs[6].default_value = 0.699
nodo_actual.inputs[7].default_value = 0.0
nodo_actual.inputs[8].default_value = 0.0
nodo_actual.inputs[9].default_value = 0.5
nodo_actual.inputs[10].default_value = 0.0
nodo_actual.inputs[11].default_value = 0.0
nodo_actual.inputs[12].default_value = 0.0
nodo_actual.inputs[13].default_value = 0.5
nodo_actual.inputs[14].default_value = 0.0
nodo_actual.inputs[15].default_value = 0.029
nodo_actual.inputs[16].default_value = 1.450
nodo_actual.inputs[17].default_value = 0.0
nodo_actual.inputs[18].default_value = 0.0
nodo_actual.inputs[19].default_value = [0.0, 0.0, 0.0, 1.0]
nodo_actual.inputs[20].default_value = 1.0
nodo_actual.inputs[21].default_value = 1.0
nodo_actual.inputs[22].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[23].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[24].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[25].default_value = 0.0

# ColorRamp_Iris_Textura es el nodo encargado de las tonalidades del iris internas
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'                
stop_actual = cr.elements.new(0.050)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(1.0)
# para crear el color blanco queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (523.012, 309.724)
nodo_actual.name = 'ColorRamp_Iris_Textura'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Bump es el nodo qotorga una especie de altura a las líneas que determinan el patrón del Iris
nodo_actual = nodos.new(type='ShaderNodeBump')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.invert = False
nodo_actual.location = (931.314, 292.384)
nodo_actual.name = 'Bump'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 0.100
nodo_actual.inputs[1].default_value = 0.100
nodo_actual.inputs[2].default_value = 1.0
nodo_actual.inputs[3].default_value = [0.0, 0.0, 0.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

######### Enlaces entre los nodos #########

enlaces.new(nodos["Mapping_Pupila"].outputs[0], nodos["Gradient_Texture_Iris_Medida"].inputs[0])    
enlaces.new(nodos["Gradient_Texture_Iris_Medida"].outputs[0], nodos["ColorRamp_Iris_Circunferencia"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Iris_Base"].outputs[3], nodos["Mapping_Pupila"].inputs[0])    
enlaces.new(nodos["Mapping_Iris"].outputs[0], nodos["Noise_Texture_Iris"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Iris_Interior"].outputs[3], nodos["Mapping_Iris"].inputs[0])    
enlaces.new(nodos["Noise_Texture_Iris"].outputs[0], nodos["ColorRamp_Iris_Interior"].inputs[0])    
enlaces.new(nodos["ColorRamp_Iris_Circunferencia"].outputs[0], nodos["Mix"].inputs[1])    
enlaces.new(nodos["ColorRamp_Iris_Interior"].outputs[0], nodos["Mix"].inputs[2])    
enlaces.new(nodos["Mix"].outputs[0], nodos["Principled BSDF"].inputs[0])    
enlaces.new(nodos["Mix"].outputs[0], nodos["ColorRamp_Iris_Textura"].inputs[0])    
enlaces.new(nodos["Principled BSDF"].outputs[0], nodos["Material Output"].inputs[0])    
enlaces.new(nodos["ColorRamp_Iris_Textura"].outputs[0], nodos["Bump"].inputs[2])    
enlaces.new(nodos["Bump"].outputs[0], nodos["Principled BSDF"].inputs[22])





####################################################################### IRIS #######################################################################

mat = bpy.data.materials.new(name='Iris_Azul_1')  # Creación del material
# Configuración del material
obj.data.materials.append(mat)  # Asignación del material

new_mat = bpy.data.materials.get('Iris_Azul_1')
if not new_mat:
    new_mat = bpy.data.materials.new('Iris_Azul_1')
   
# habilitaremos el uso de nodos, ya que sin ello no podríamos crear ninguno
new_mat.use_nodes = True

# Definimos la estructura que tendran los nodos y los enlaces para su creación
node_tree = new_mat.node_tree
nodos = node_tree.nodes
nodos.clear()
    
enlaces = node_tree.links
enlaces.clear()
    
######### Nodos #########

# Mapping_Pupila determina el radio de la pupila
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-760.619, 177.171)
nodo_actual.name = 'Mapping_Pupila'
nodo_actual.vector_type = 'POINT'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.649, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 1.0, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Gradient_Texture_Iris_Medida es el nodo que muestrea la textura, al estar en modo esférico crea un degradado inverso utilizando el vector de Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexGradient')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.gradient_type = 'SPHERICAL'
nodo_actual.location = (-470.620, 115.160)
nodo_actual.name = 'Gradient_Texture_Iris_Medida'
nodo_actual.width = 140.0

# Texture_Coordinate_Iris_Base utilizando las coordenadas del espacio objeto el cual irá al nodo Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-970.619, 160.171)
nodo_actual.name = 'Texture_Coordinate_Iris_Base'
nodo_actual.object = None
nodo_actual.width = 140.0

# Texture_Coordinate_Iris_Interior utilizando las coordenadas del espacio objeto el cual irá al nodo Mapping_Pupila
nodo_actual = nodos.new(type='ShaderNodeTexCoord')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.from_instancer = False
nodo_actual.location = (-987.080, 524.705)
nodo_actual.name = 'Texture_Coordinate_Iris_Interior'
nodo_actual.object = None
nodo_actual.width = 140.0

# Mapping_Iris es el nodo utilizado para las "líneas" del Iris
nodo_actual = nodos.new(type='ShaderNodeMapping')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-777.080, 541.705)
nodo_actual.name = 'Mapping_Iris'
nodo_actual.vector_type = 'NORMAL'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = [1.0, 15.600, 1.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

# Noise_Texture_Iris es el nodo que trata la distorsión y lo nítido que es el Iris
nodo_actual = nodos.new(type='ShaderNodeTexNoise')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (-480.180, 462.844)
nodo_actual.name = 'Noise_Texture_Iris'
nodo_actual.noise_dimensions = '3D'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = 5.0
nodo_actual.inputs[3].default_value = 10.0
nodo_actual.inputs[4].default_value = 0.5
nodo_actual.inputs[5].default_value = 2.5
nodo_actual.outputs[0].default_value = 0.0
nodo_actual.outputs[1].default_value = [0.0, 0.0, 0.0, 0.0]

# ColorRamp_Iris_Interior es el nodo encargado de las tonalidades de azul en el interior del iris
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'
stop_actual = cr.elements.new(0.350)
# para crear el color azul claro queremos en RGB los valores 0.420, 0.700, 0.700 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.420, 0.700, 0.700, 1.0]
stop_actual = cr.elements.new(0.600)
# para crear el color azul oscuro queremos en RGB los valores 0.120, 0.232, 0.400 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.120, 0.232, 0.400, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-235.032, 521.752)
nodo_actual.name = 'ColorRamp_Iris_Interior'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# ColorRamp_Iris_Circunferencia es el nodo encargado de las tonalidades de azul en el interior del iris
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'EASE'                
stop_actual = cr.elements.new(0.5)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(0.550)
# para crear el color azul oscuro queremos en RGB los valores 0.020, 0.028, 0.100 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.020, 0.028, 0.100, 1.0]
stop_actual = cr.elements.new(0.620)
# para crear el color azul oscuro pálido queremos en RGB los valores 0.120, 0.152, 0.200 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.120, 0.152, 0.200, 1.0]
stop_actual = cr.elements.new(0.700)
# para crear el color azul claro queremos en RGB los valores 0.020, 0.028, 0.100 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.302, 0.476, 0.550, 1.0]
stop_actual = cr.elements.new(0.760)
# para crear el color azul oscuro pálido queremos en RGB los valores 0.120, 0.152, 0.200 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.087, 0.133, 0.25, 1.0]
stop_actual = cr.elements.new(0.764)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (-237.990, 246.606)
nodo_actual.name = 'ColorRamp_Iris_Circunferencia'
nodo_actual.width = 244.526
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Mix es el nodo que mezcla de modo superpuesto ColorRamp_Iris_Interior con ColorRamp_Iris_Circunferencia para dar ese patrón al iris 
nodo_actual = nodos.new(type='ShaderNodeMixRGB')
nodo_actual.blend_type = 'OVERLAY'
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.location = (281.812, 481.425)
nodo_actual.name = 'Mix'
nodo_actual.use_alpha = False
nodo_actual.use_clamp = False
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 1.0

# Material Output es el nodo encargado de que todos los nodos hagan efecto en la mesh, sin él no se vería reflejado en la aplicación de Blender
nodo_actual = nodos.new(type='ShaderNodeOutputMaterial')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.is_active_output = True
nodo_actual.location = (1551.203, 451.363)
nodo_actual.name = 'Material Output'
nodo_actual.target = 'ALL'
nodo_actual.width = 140.0
nodo_actual.inputs[2].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[3].default_value = 0.0

# Principled BSDF es el nodo que se crea por defecto en el cual se aplicará el nodo Mix en el color Base y el Bump para la nitidez del iris
nodo_actual = nodos.new(type='ShaderNodeBsdfPrincipled')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.distribution = 'GGX'
nodo_actual.location = (1213.195, 444.630)
nodo_actual.name = 'Principled BSDF'
nodo_actual.subsurface_method = 'BURLEY'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = [0.008, 0.0, 0.800, 1.0]
nodo_actual.inputs[1].default_value = 0.0
nodo_actual.inputs[2].default_value = [1.0, 0.200, 0.100]
nodo_actual.inputs[3].default_value = [0.800, 0.800, 0.800, 1.0]
nodo_actual.inputs[4].default_value = 1.399
nodo_actual.inputs[5].default_value = 0.0
nodo_actual.inputs[6].default_value = 0.699
nodo_actual.inputs[7].default_value = 0.0
nodo_actual.inputs[8].default_value = 0.0
nodo_actual.inputs[9].default_value = 0.5
nodo_actual.inputs[10].default_value = 0.0
nodo_actual.inputs[11].default_value = 0.0
nodo_actual.inputs[12].default_value = 0.0
nodo_actual.inputs[13].default_value = 0.5
nodo_actual.inputs[14].default_value = 0.0
nodo_actual.inputs[15].default_value = 0.029
nodo_actual.inputs[16].default_value = 1.450
nodo_actual.inputs[17].default_value = 0.0
nodo_actual.inputs[18].default_value = 0.0
nodo_actual.inputs[19].default_value = [0.0, 0.0, 0.0, 1.0]
nodo_actual.inputs[20].default_value = 1.0
nodo_actual.inputs[21].default_value = 1.0
nodo_actual.inputs[22].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[23].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[24].default_value = [0.0, 0.0, 0.0]
nodo_actual.inputs[25].default_value = 0.0

# ColorRamp_Iris_Textura es el nodo encargado de las tonalidades del iris internas
nodo_actual = nodos.new(type='ShaderNodeValToRGB')
nodo_actual.color = (0.608, 0.608, 0.608)
cr = nodo_actual.color_ramp
cr.color_mode = 'RGB'
cr.hue_interpolation = 'NEAR'
cr.interpolation = 'LINEAR'                
stop_actual = cr.elements.new(0.050)
# para crear el color negro queremos en RGB los valores 0.0, 0.0, 0.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [0.0, 0.0, 0.0, 1.0]
stop_actual = cr.elements.new(1.0)
# para crear el color blanco queremos en RGB los valores 1.0, 1.0, 1.0 y el 1.0 hace alusión a la opacidad siendo 1.0 completamente opaco y 0.0 sería transparente
stop_actual.color = [1.0, 1.0, 1.0, 1.0]
removed_black = removed_white = False
# Esta parte de código es necesaria para que no se creen los puntos de parada de los extremos (color negro puro y blanco puro)
for i in range(len(cr.elements) - 1, -1, -1):
    stop = cr.elements[i]
    if not removed_black and stop.position == 0 and all([stop.color[i] == (0, 0, 0, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_black = True
    if not removed_white and stop.position == 1 and all([stop.color[i] == (1, 1, 1, 1)[i] for i in range(4)]):
        cr.elements.remove(stop)
        removed_white = True                
nodo_actual.location = (523.012, 309.724)
nodo_actual.name = 'ColorRamp_Iris_Textura'
nodo_actual.width = 240.0
nodo_actual.inputs[0].default_value = 0.5
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0, 0.0]
nodo_actual.outputs[1].default_value = 0.0

# Bump es el nodo qotorga una especie de altura a las líneas que determinan el patrón del Iris
nodo_actual = nodos.new(type='ShaderNodeBump')
nodo_actual.color = (0.608, 0.608, 0.608)
nodo_actual.invert = False
nodo_actual.location = (931.314, 292.384)
nodo_actual.name = 'Bump'
nodo_actual.width = 140.0
nodo_actual.inputs[0].default_value = 0.100
nodo_actual.inputs[1].default_value = 0.100
nodo_actual.inputs[2].default_value = 1.0
nodo_actual.inputs[3].default_value = [0.0, 0.0, 0.0]
nodo_actual.outputs[0].default_value = [0.0, 0.0, 0.0]

######### Enlaces entre los nodos #########

enlaces.new(nodos["Mapping_Pupila"].outputs[0], nodos["Gradient_Texture_Iris_Medida"].inputs[0])    
enlaces.new(nodos["Gradient_Texture_Iris_Medida"].outputs[0], nodos["ColorRamp_Iris_Circunferencia"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Iris_Base"].outputs[3], nodos["Mapping_Pupila"].inputs[0])    
enlaces.new(nodos["Mapping_Iris"].outputs[0], nodos["Noise_Texture_Iris"].inputs[0])    
enlaces.new(nodos["Texture_Coordinate_Iris_Interior"].outputs[3], nodos["Mapping_Iris"].inputs[0])    
enlaces.new(nodos["Noise_Texture_Iris"].outputs[0], nodos["ColorRamp_Iris_Interior"].inputs[0])    
enlaces.new(nodos["ColorRamp_Iris_Circunferencia"].outputs[0], nodos["Mix"].inputs[1])    
enlaces.new(nodos["ColorRamp_Iris_Interior"].outputs[0], nodos["Mix"].inputs[2])    
enlaces.new(nodos["Mix"].outputs[0], nodos["Principled BSDF"].inputs[0])    
enlaces.new(nodos["Mix"].outputs[0], nodos["ColorRamp_Iris_Textura"].inputs[0])    
enlaces.new(nodos["Principled BSDF"].outputs[0], nodos["Material Output"].inputs[0])    
enlaces.new(nodos["ColorRamp_Iris_Textura"].outputs[0], nodos["Bump"].inputs[2])    
enlaces.new(nodos["Bump"].outputs[0], nodos["Principled BSDF"].inputs[22])    

# Definimos los vértices que comprenden el iris en vertices_Iris
bpy.context.object.active_material_index = 1
vertices_Iris = [15,30,45,60,75,90,105,120,136,151,167,182,197,212,227,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290]        

# Bucle para seleccionar los vértices definidos en la lista vertices_Iris
for i in range(len(vertices_Iris)):
     obj.data.vertices[vertices_Iris[i]].select = True

bpy.ops.object.mode_set(mode = 'EDIT')

# Asignamos el material Iris a los vértices seleccionados
bpy.ops.object.material_slot_assign()
bpy.ops.object.mode_set(mode = 'OBJECT')