import pymeshlab
ms = pymeshlab.MeshSet()

base_path = '/home/gyuseok/catkin_ws_kitti/result_data/'
ms.load_new_mesh(base_path + 'ford_mapping_rgb.ply')
print(ms.number_meshes())

text_dim = 2048

ms.compute_normals_for_point_sets(k=15, smoothiter=5, flipflag=False, viewpos=[0, 0, 0])
ms.surface_reconstruction_screened_poisson(depth=8, fulldepth=6)
ms.select_faces_with_edges_longer_than(threshold=1)
ms.delete_selected_faces_and_vertices()
ms.remove_isolated_pieces_wrt_face_num(mincomponentsize=5)
ms.select_non_manifold_vertices()
ms.delete_selected_faces_and_vertices()
ms.per_vertex_texture_function()
ms.convert_pervertex_uv_into_perwedge_uv()
ms.parametrization_trivial_per_triangle(textdim=text_dim, method='Basic')

ms.save_current_mesh(file_name=base_path + "meshlab_test.obj", save_vertex_normal=True)

ms.transfer_vertex_color_to_texture(textname="pymeshlab_test.png", textw=text_dim, texth=text_dim, assign=True)

