import bpy
from datetime import datetime

# Global list to store recorded actions
recorded_actions = []

# Operator to toggle recording
class RecordMacroOperator(bpy.types.Operator):
    bl_idname = "wm.record_macro"
    bl_label = "Start/Stop Macro Recording"

    recording = False  # Class variable to track the recording state

    def execute(self, context):
        if not RecordMacroOperator.recording:
            # Start recording
            self.report({'INFO'}, "Recording started...")
            RecordMacroOperator.recording = True
            bpy.app.handlers.depsgraph_update_post.append(record_macro)
        else:
            # Stop recording and export to a text block
            self.report({'INFO'}, "Recording stopped. Exporting to text block...")
            RecordMacroOperator.recording = False
            bpy.app.handlers.depsgraph_update_post.remove(record_macro)
            self.export_to_text_block(context)
        return {'FINISHED'}

    def export_to_text_block(self, context):
        # Create a new text block in Blender's Text Editor
        text_block = bpy.data.texts.new("Recorded_Macro")
        for action in recorded_actions:
            text_block.write(action + "\n")
        self.report({'INFO'}, "Recorded macro saved to a text block.")

# Function to record macro actions with timestamp
def record_macro(scene):
    # Check if there is an active operator and store its details
    if bpy.context.active_operator:
        op_name = bpy.context.active_operator.bl_idname
        op_params = ", ".join([f"{prop}={repr(value)}" for prop, value in bpy.context.active_operator.properties.items()])
        
        # Get the current timestamp
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Store the action string with the timestamp
        action_str = f"[{current_time}] bpy.ops.{op_name}({op_params})"
        
        if action_str not in recorded_actions:
            recorded_actions.append(action_str)

# Panel for the UI in the 3D View
class VIEW3D_PT_MacroRecorder(bpy.types.Panel):
    bl_label = "Macro Recorder"
    bl_idname = "VIEW3D_PT_macro_recorder"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Macro Recorder'

    def draw(self, context):
        layout = self.layout
        layout.operator(RecordMacroOperator.bl_idname, text="Start/Stop Recording")

# Register and unregister functions
def register():
    bpy.utils.register_class(RecordMacroOperator)
    bpy.utils.register_class(VIEW3D_PT_MacroRecorder)

def unregister():
    bpy.utils.unregister_class(RecordMacroOperator)
    bpy.utils.unregister_class(VIEW3D_PT_MacroRecorder)

if __name__ == "__main__":
    register()
