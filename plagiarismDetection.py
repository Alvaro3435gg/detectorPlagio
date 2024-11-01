def largest_common_substrings_top5_with_suffix_arrays(suffix_array1, suffix_array2, text1, text2):
    """
    Encuentra las 5 subcadenas comunes más largas entre dos textos utilizando arrays de sufijos
    y evitando superposiciones.
    """
    def common_substring_from_suffixes(suffix1, suffix2):
        """
        Calcula la longitud de la subcadena común que comienza en los índices especificados por los sufijos.
        """
        i, j = suffix1, suffix2
        common_length = 0
        while i < len(text1) and j < len(text2) and text1[i] == text2[j]:
            common_length += 1
            i += 1
            j += 1
        return text1[suffix1:suffix1 + common_length]

    substrings = []
    used_ranges_text1 = set()

    for suffix1 in suffix_array1:
        for suffix2 in suffix_array2:
            substring = common_substring_from_suffixes(suffix1, suffix2)
            if substring and len(substring) > 0:
                # Verificar que la subcadena no esté superpuesta con rangos previos
                end_pos = suffix1 + len(substring)
                if all(not (suffix1 < r[1] and end_pos > r[0]) for r in used_ranges_text1):
                    substrings.append((substring, len(substring)))
                    used_ranges_text1.add((suffix1, end_pos))
                    # Ordenar y mantener solo las 5 subcadenas más largas
                    substrings = sorted(substrings, key=lambda x: -x[1])[:5]

    # Extraer solo las subcadenas (sin longitud)
    return [s[0] for s in substrings]
