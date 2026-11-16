import unittest
from unittest.mock import patch
from main import anadir_tarea, eliminar_tarea


class TestFocusQuest(unittest.TestCase):

    @patch("main.guardar_tareas")
    def test_anadir_tarea(self, guardar_falso):
        tareas = []

        resultado = anadir_tarea(tareas, "estudiar")

        self.assertEqual(resultado, "anadida")
        self.assertIn("estudiar", tareas)
        guardar_falso.assert_called_once_with(tareas)

    @patch("main.guardar_tareas")
    def test_tarea_duplicada(self, guardar_falso):
        tareas = ["estudiar"]

        resultado = anadir_tarea(tareas, "estudiar")

        self.assertEqual(resultado, "dupe")
        self.assertEqual(len(tareas), 1)
        guardar_falso.assert_not_called()

    @patch("main.guardar_tareas")
    def test_tarea_vacia(self, guardar_falso):
        tareas = []

        resultado = anadir_tarea(tareas, "")

        self.assertEqual(resultado, "vacía")
        self.assertEqual(tareas, [])
        guardar_falso.assert_not_called()

    @patch("main.guardar_tareas")
    def test_eliminar_existente(self, guardar_falso):
        tareas = ["estudiar", "programar"]

        resultado = eliminar_tarea(tareas, "estudiar")

        self.assertTrue(resultado)
        self.assertEqual(tareas, ["programar"])
        guardar_falso.assert_called_once_with(tareas)

    @patch("main.guardar_tareas")
    def test_eliminar_inexistente(self, guardar_falso):
        tareas = ["estudiar"]

        resultado = eliminar_tarea(tareas, "dormir")

        self.assertFalse(resultado)
        self.assertEqual(tareas, ["estudiar"])
        guardar_falso.assert_not_called()


if __name__ == "__main__":
    unittest.main()
