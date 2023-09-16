SELECT pl.name, base.key, utext.textlabel, trans.trans 
FROM api_base base 
INNER JOIN api_basetext btext ON base.id = btext.base_id 
INNER JOIN api_uniquetext utext ON btext.uniquetext_id = utext.id
INNER JOIN api_platform pl ON pl.id = base.platform_id
INNER JOIN api_translation trans ON trans.uniquetext_id = btext.uniquetext_id
WHERE trans.language_id = 3

