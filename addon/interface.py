def draw(self, context):

  layout = self.layout

  column = layout.column(align=True)

  column.separator()

  column.label(text='Selection Bounds:')

  column.prop(context.scene.selection_bounds, 'mode', text='')

  if context.scene.selection_bounds.mode != 'NONE':

    row = column.row(align=True)

    if context.scene.selection_bounds.use_object_color:

      row.prop(context.object, 'color', text='')

    else:

      row.prop(context.scene.selection_bounds, 'color', text='')

    row.prop(context.scene.selection_bounds, 'use_object_color', text='', icon='OBJECT_DATA')

    column.prop(context.scene.selection_bounds, 'width')

    column.prop(context.scene.selection_bounds, 'length', slider=True)
