from django.test import SimpleTestCase

# Create your tests here.
from django.urls import reverse

class SnacksTest(SimpleTestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'home.html')
        self.assertTemplateUsed(response,'base.html')

    def test_about_page_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_about_page_template(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'about.html')
        self.assertTemplateUsed(response,'base.html')

    def test_foodgroups_page_status_code(self):
        url = reverse('foodgroups')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_foodgroups_page_template(self):
        url = reverse('foodgroups')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'foodgroups.html')
        self.assertTemplateUsed(response,'base.html')

    def test_meals_page_status_code(self):
        url = reverse('meals')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_meals_page_template(self):
        url = reverse('meals')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'meals.html')
        self.assertTemplateUsed(response,'base.html')

    def test_snacks_page_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_snacks_page_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snacks.html')
        self.assertTemplateUsed(response,'base.html')