import bpy

class LightOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.simple_operator"
    bl_label = "Spawn Light by Trina"

    # Method to place the lights
    def placeLights(self, context):
        bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(1.91971, 3.53555, -0.657626), scale=(1, 1, 1))
        bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(-8.00828,-10.2035, 6.43074), scale=(1, 1, 1))
        bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(-8.00828, 10.2035, 6.43074), scale=(1, 1, 1))

    # 'execute' method that will be called when the operator is run
    def execute(self, context):
        self.placeLights(context)
        return {'FINISHED'}

# Add operator to the menu
def menu_func(self, context):
    self.layout.operator(LightOperator.bl_idname, text=LightOperator.bl_label)






