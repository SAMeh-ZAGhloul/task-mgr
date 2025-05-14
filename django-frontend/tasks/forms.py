from django import forms

class TaskForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 border border-slate-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition duration-150',
            'placeholder': 'e.g., Implement user authentication'
        })
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'w-full p-3 border border-slate-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition duration-150',
            'placeholder': 'Detailed description of the task...',
            'rows': 3
        })
    )
    aiInstructions = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'w-full p-3 border border-slate-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition duration-150',
            'placeholder': 'Specific instructions for AI if applicable...',
            'rows': 3
        })
    )
    priority = forms.ChoiceField(
        choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')],
        initial='Medium',
        widget=forms.Select(attrs={
            'class': 'w-full p-3 border border-slate-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition duration-150'
        })
    )
    assignedTo = forms.CharField(
        initial='AI',
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 border border-slate-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition duration-150',
            'placeholder': 'e.g., AI Assistant, John Doe'
        })
    )
    dueDate = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'w-full p-3 border border-slate-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition duration-150'
        })
    )
