def draw(self, context):

  layout = self.layout

  addon = context.user_preferences.addons[__name__.partition('.')[0]]

  option = context.scene.selected_bounds if addon.preferences.scene_independent else addon.preferences

  column = layout.column(align=True)

  column.separator()

  column.label(text='Selected Bounds:')

  if not context.window_manager.running_modal.selected_bounds:

    column.operator('view3d.selected_bounds', text='Enable')

  else:

    column.prop(option, 'mode', text='')

    if addon.preferences.scene_independent or addon.preferences.display_preferences:
      if option.mode != 'NONE':

        row = column.row(align=True)

        if context.object and option.use_object_color:

          row.prop(context.object, 'color', text='')

        else:

          row.prop(option, 'color', text='')

        row.prop(option, 'use_object_color', text='', icon='OBJECT_DATA')

        column.prop(option, 'width')

        column.prop(option, 'length', slider=True)
