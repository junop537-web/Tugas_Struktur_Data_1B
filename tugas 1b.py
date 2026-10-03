from collections import deque
import unittest

class Mahasiswa:

  def __init__(self, nomor_urut: str, nama: str):
    self.nomor_urut = nomor_urut
    self.nama = nama

  def __repr__(self):
    return f"[{self.nomor_urut}] {self.nama}"


class SistemAntrean:

  def __init__(self):
    self._queue = deque()

  def enqueue(self, mahasiswa: Mahasiswa):
    self._queue.append(mahasiswa)

  def dequeue(self) -> Mahasiswa:
    if not self.is_empty():
      return self._queue.popleft()
    return None

  def front(self) -> Mahasiswa:
    if not self.is_empty():
      return self._queue[0]
    return None

  def is_empty(self) -> bool:
    return len(self._queue) == 0

  def get_all(self):
    return list(self._queue)


class FiturUndo:

  def __init__(self):
    self._stack = []

  def push(self, aktivitas: str):
    self._stack.append(aktivitas)

  def pop(self) -> str:
    if not self.is_empty():
      return self._stack.pop()
    return None

  def top(self) -> str:
    if not self.is_empty():
      return self._stack[-1]
    return None

  def is_empty(self) -> bool:
    return len(self._stack) == 0

  def get_all(self):
    return list(self._stack)


def jalankan_simulasi():
  print("=" * 65)
  print("SIMULASI SISTEM ANTREAN & FITUR UNDO".center(65))
  print("=" * 65)

  antrean = SistemAntrean()
  undo_stack = FiturUndo()

  mhs_list = [
      Mahasiswa("001", "Hakim Wijaya"),
      Mahasiswa("002", "Sidiq Santoso"),
      Mahasiswa("003", "Marsya Jeny"),
      Mahasiswa("004", "Indriyani"),
      Mahasiswa("005", "Irfan Pratama"),
  ]

  print("\n--- 1. SIMULASI FITUR ANTREAN (QUEUE) ---")
  for mhs in mhs_list:
    antrean.enqueue(mhs)
    undo_stack.push(f"Menambahkan Antrean Mahasiswa {mhs.nomor_urut}")
    print(
        f"[Enqueue] {mhs} masuk ke antrean. | Isi Antrean: {antrean.get_all()}"
    )

  print(f"\n[Front/Peek] Mahasiswa di depan antrean saat ini: {antrean.front()}")

  print("\nMelayani Mahasiswa Terdepan...")
  mhs_dilayani = antrean.dequeue()
  undo_stack.push(f"Melayani Mahasiswa {mhs_dilayani.nomor_urut}")
  print(
      f"[Dequeue] {mhs_dilayani} telah dilayani. | Sisa Antrean:"
      f" {antrean.get_all()}"
  )

  print("\n--- 2. SIMULASI FITUR UNDO (STACK) ---")
  print("Riwayat Aktivitas Terdaftar:")
  for idx, akt in enumerate(undo_stack.get_all(), 1):
    print(f"  {idx}. {akt}")

  print(f"\n[Top/Peek] Aktivitas Terakhir: '{undo_stack.top()}'")

  aksi_dibatalkan = undo_stack.pop()
  print(f"[Pop / Undo] Membatalkan aktivitas -> '{aksi_dibatalkan}'")
  print(f"Sisa Stack Undo: {undo_stack.get_all()}")


class TestSistemAntreanDanUndo(unittest.TestCase):

  def setUp(self):
    self.antrean = SistemAntrean()
    self.undo = FiturUndo()

  def test_queue_operations(self):
    self.assertTrue(self.antrean.is_empty())

    m1 = Mahasiswa("001", "Hakim Sanjaya")
    m2 = Mahasiswa("002", "Sidiq Santoso")

    self.antrean.enqueue(m1)
    self.antrean.enqueue(m2)
    self.assertFalse(self.antrean.is_empty())
    self.assertEqual(self.antrean.front(), m1)

    dilayani = self.antrean.dequeue()
    self.assertEqual(dilayani, m1)
    self.assertEqual(self.antrean.front(), m2)

  def test_stack_undo_operations(self):
    self.assertTrue(self.undo.is_empty())

    self.undo.push("Menambahkan Antrean Mahasiswa 001")
    self.undo.push("Menambahkan Antrean Mahasiswa 002")
    self.assertFalse(self.undo.is_empty())
    self.assertEqual(self.undo.top(), "Menambahkan Antrean Mahasiswa 002")

    batal = self.undo.pop()
    self.assertEqual(batal, "Menambahkan Antrean Mahasiswa 002")
    self.assertEqual(self.undo.top(), "Menambahkan Antrean Mahasiswa 001")


if __name__ == "__main__":
  jalankan_simulasi()
  print("\n" + "=" * 65)
  print("MENJALANKAN UNIT TESTING...".center(65))
  print("=" * 65)
  unittest.main(exit=False)