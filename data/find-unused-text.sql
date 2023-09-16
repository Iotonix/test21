-- SQLite
SELECT id, created, textlabel
FROM api_uniquetext a
WHERE a.id NOT IN (
    SELECT uniquetext_id 
    FROM api_translation
);
