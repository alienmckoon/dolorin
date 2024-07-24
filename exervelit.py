# Example of a more complex data structure
statistics = {
    'folders': {
        'total': total_folders_count,
        'details': [
            {'name': 'Folder1', 'size': '10MB'},
            {'name': 'Folder2', 'size': '20MB'}
        ]
    },
    'files': {
        'total': 150,
        'types': {
            'images': 50,
            'documents': 100
        }
    }
}

print(statistics)
# Output:
# {
#     'folders': {
#         'total': 42,
#         'details': [{'name': 'Folder1', 'size': '10MB'}, {'name': 'Folder2', 'size': '20MB'}]
#     },
#     'files': {
#         'total': 150,
#         'types': {'images': 50, 'documents': 100}
#     }
# }
