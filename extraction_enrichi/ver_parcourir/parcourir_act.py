import xml.etree.ElementTree as ET
import html
import os

def get_element_text(element):
    """Récupère récursivement le texte de l'élément et de ses éléments enfants."""
    text = element.text or ""
    for child in element:
        text += get_element_text(child)
        if child.tail:
            text += child.tail
    return text.strip()


def extract_act_content_to_tsv(directory_path, output_path):
    """Parcourt tous les fichiers XML dans le dossier spécifié, extrait le contenu act et le sauvegarde dans un fichier TSV."""
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write("Nom_fichier\tNuméro_Phrase\tDynamique\tSegment_Annoté\tType\n")

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(".xml"):
                    file_path = os.path.join(root, file)
                    nom_fichier = os.path.basename(file_path)
                    tree = ET.parse(file_path)
                    root_element = tree.getroot()

                    for i, phrase in enumerate(root_element.findall('.//phrase'), start=1):
                        dyns = phrase.findall('.//dyn')
                        acts = phrase.findall('.//act')

                        # Faire correspondre les dyns et les acts en fonction de l'attribut n ou de la relation interne
                        dyn_map = {dyn.get('n'): dyn for dyn in dyns if dyn.get('n')}
                        default_dyn = [dyn for dyn in dyns if not dyn.get('n')]

                        for act in acts:
                            act_text = html.unescape(get_element_text(act)).strip()
                            act_type = act.get('type', '').strip()
                            act_n = act.get('n')

                            if act_n:
                                matched_dyns = [dyn_map[n] for n in act_n.split('+') if n in dyn_map]
                            else:
                                # Vérifier si l'act est imbriqué dans un dyn
                                parent_dyn = next((dyn for dyn in dyns if act in list(dyn.iter())), None)
                                if parent_dyn:
                                    matched_dyns = [parent_dyn]
                                else:
                                    matched_dyns = default_dyn  # Si l'act n'a pas d'attribut n et n'est pas imbriqué, le lier à tous les dyns sans attribut n

                            for dyn in matched_dyns:
                                dyn_text = html.unescape(get_element_text(dyn)).strip()
                                output_line = f"{nom_fichier}\t{i}\t{dyn_text}\t{act_text}\t{act_type}\n"
                                output_file.write(output_line)

directory_path = '../../corpus_xml/CE'
output_file_path = 'all_acts.tsv'

extract_act_content_to_tsv(directory_path, output_file_path)
print(f"Data extracted to: {output_file_path}")
