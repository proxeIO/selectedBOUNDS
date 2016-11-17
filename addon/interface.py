def draw(self, context):

  layout = self.layout

  addon = context.user_preferences.addons[__name__.partition('.')[0]].preferences

  column = layout.column(align=True)

  column.separator()

  column.label(text='Selected Bounds:')

  if addon.scene_independent:

    column.prop(context.scene.selected_bounds, 'mode', text='')

  else:

    column.prop(addon, 'mode', text='')

  if addon.scene_independent and context.scene.selected_bounds.mode != 'NONE':

    row = column.row(align=True)

    if context.object and context.scene.selected_bounds.use_object_color:

      row.prop(context.object, 'color', text='')

    else:

      row.prop(context.scene.selected_bounds, 'color', text='')

    row.prop(context.scene.selected_bounds, 'use_object_color', text='', icon='OBJECT_DATA')

    column.prop(context.scene.selected_bounds, 'width')

    column.prop(context.scene.selected_bounds, 'length', slider=True)
